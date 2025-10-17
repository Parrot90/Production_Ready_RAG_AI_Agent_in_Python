import logging
from fastapi import FastAPI
import inngest
import inngest.fast_api
from dotenv import load_dotenv
import uuid
import os
import datetime
from data_loader import load_and_chunk_pdf, embed_texts
from vector_db import QdrantStorage
from custom_types import RAQQueryResult, RAGSearchResult, RAGUpsertResult, RAGChunkAndSrc
from transformers import pipeline
load_dotenv()
inngest_client = inngest.Inngest(
app_id="rag_app",
logger=logging.getLogger("uvicorn"),
is_production=False,
serializer=inngest.PydanticSerializer()

)
#decorator to create the function
@inngest_client.create_function(
    fn_id="rag_event",
    trigger=inngest.TriggerEvent(event="rag/ingest_pdf")
)
async def rag_ingest_pdf(ctx: inngest.Context):
    def _load(ctx: inngest.Context) -> RAGChunkAndSrc:
        pdf_path = ctx.event.data.get("pdf_path", "")
        # prefer explicit source_id, otherwise use pdf_path, otherwise generate a uuid
        source_id = ctx.event.data.get("source_id") or pdf_path or str(uuid.uuid4())
        chunks = load_and_chunk_pdf(pdf_path)
        return RAGChunkAndSrc(chunks=chunks, source_id=source_id)
    
    def _upsert(chunks_and_src: RAGChunkAndSrc) -> RAGUpsertResult:
        chunks = chunks_and_src.chunks
        source_id = chunks_and_src.source_id
        vecs = embed_texts(chunks)
        ids = [str(uuid.uuid5(uuid.NAMESPACE_URL, f"{source_id}-{i}")) for i in range(len(chunks))]
        payloads = [{"source": source_id, "text": chunks[i]} for i in range(len(chunks))]
        QdrantStorage().upsert(ids, vecs, payloads)
        return RAGUpsertResult(ingested=len(chunks))

    chunks_and_src = await ctx.step.run("load-and-chunk", lambda: _load(ctx), output_type=RAGChunkAndSrc)
    ingested = await ctx.step.run("embed-and-upsert", lambda: _upsert(chunks_and_src), output_type=RAGUpsertResult)
    return ingested.model_dump()

app = FastAPI()
inngest.fast_api.serve(app, inngest_client, functions=[rag_ingest_pdf])

# @inngest_client.create_function(
#     fn_id="RAG: Query PDF",
#     trigger=inngest.TriggerEvent(event="rag/query_pdf_ai")
# )
# async def rag_query_pdf_ai(ctx: inngest.Context):
#     def _search(question: str, top_k: int=5):
#         query_vec = embed_texts([question])[0]
#         store = QdrantStorage()
#         found = store.search(query_vec, top_k=top_k)
#         return RAGSearchResult(contexts=found["contexts"], sources=found["sources"])
    
#     def _generate_answer(question: str, contexts: list[str]) -> str:
#         from transformers import pipeline
        
#         # Load a local LLM (first run will download ~3-7GB model)
#         generator = pipeline(
#             "text-generation",
#             model="microsoft/Phi-3-mini-4k-instruct",  # Small, fast, good quality
#             device="cpu"  # or "cuda" if you have GPU
#         )
        
#         context_block = "\n\n".join(f"- {c}" for c in contexts)
#         prompt = (
#             "Use the following context to answer the question.\n\n"
#             f"Context:\n{context_block}\n\n"
#             f"Question: {question}\n\n"
#             "Answer concisely using only the context above:"
#         )
        
#         response = generator(
#             prompt,
#             max_new_tokens=512,
#             temperature=0.2,
#             do_sample=True
#         )
        
#         return response[0]["generated_text"].split("Answer concisely using only the context above:")[-1].strip()
    
#     question = ctx.event.data.get("question", "")
#     top_k = ctx.event.data.get("top_k", 5)
    
#     found = await ctx.step.run("embed-and-search", lambda: _search(question, top_k), output_type=RAGSearchResult)
#     answer = await ctx.step.run("llm-answer", lambda: _generate_answer(question, found.contexts))
    
#     return {"answer": answer, "sources": found.sources, "num_contexts": len(found.contexts)}


@inngest_client.create_function(
    fn_id="RAG: Query PDF",
    trigger=inngest.TriggerEvent(event="rag/query_pdf_ai")
)
async def rag_query_pdf_ai(ctx: inngest.Context):
    def _search(question: str, top_k: int=5):
        query_vec = embed_texts([question])[0]
        store = QdrantStorage()
        found = store.search(query_vec, top_k=top_k)
        return RAGSearchResult(contexts=found["contexts"], sources=found["sources"])
    
    def _generate_answer(question: str, contexts: list[str]) -> str:
        import requests
        
        context_block = "\n\n".join(f"- {c}" for c in contexts)
        prompt = (
            "Use the following context to answer the question.\n\n"
            f"Context:\n{context_block}\n\n"
            f"Question: {question}\n\n"
            "Answer concisely using only the context above."
        )
        
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3:latest", 
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.2,
                    "num_predict": 512
                }
            }
        )

        return response.json()["response"].strip()
    
    question = ctx.event.data.get("question", "")
    top_k = ctx.event.data.get("top_k", 5)
    
    found = await ctx.step.run("embed-and-search", lambda: _search(question, top_k), output_type=RAGSearchResult)
    answer = await ctx.step.run("llm-answer", lambda: _generate_answer(question, found.contexts))
    
    return {"answer": answer, "sources": found.sources, "num_contexts": len(found.contexts)}

app = FastAPI()

inngest.fast_api.serve(app, inngest_client, [rag_ingest_pdf, rag_query_pdf_ai])

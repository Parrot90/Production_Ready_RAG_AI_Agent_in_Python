
================================================
FILE: README.md
================================================

Directory structure:
└── parrot90-production_ready_rag_ai_agent_in_python/
    ├── README.md
    ├── custom_types.py
    ├── data_loader.py
    ├── main.py
    ├── pyproject.toml
    ├── streamlit_app.py
    ├── vector_db.py
    ├── .python-version
    └── qdrant_storage/
        ├── raft_state.json
        ├── .qdrant_fs_check
        ├── aliases/
        │   └── data.json
        └── collections/
            └── docs/
                ├── config.json
                ├── shard_key_mapping.json
                ├── version.info
                └── 0/
                    ├── newest_clocks.json
                    ├── replica_state.json
                    ├── shard_config.json
                    ├── segments/
                    │   ├── 492da1fa-d1ba-442d-bb6a-137ac4819cac/
                    │   │   ├── segment.json
                    │   │   ├── version.info
                    │   │   ├── payload_index/
                    │   │   │   ├── config.json
                    │   │   │   ├── CURRENT
                    │   │   │   ├── IDENTITY
                    │   │   │   ├── LOCK
                    │   │   │   ├── LOG
                    │   │   │   ├── MANIFEST-000005
                    │   │   │   └── OPTIONS-000007
                    │   │   ├── payload_storage/
                    │   │   │   ├── bitmask.dat
                    │   │   │   ├── config.json
                    │   │   │   └── gaps.dat
                    │   │   └── vector_storage/
                    │   │       ├── deleted/
                    │   │       │   └── status.dat
                    │   │       └── vectors/
                    │   │           ├── config.json
                    │   │           └── status.dat
                    │   ├── 6fe14414-520d-44ca-aac7-c286c5d37049/
                    │   │   ├── segment.json
                    │   │   ├── version.info
                    │   │   ├── payload_index/
                    │   │   │   ├── config.json
                    │   │   │   ├── CURRENT
                    │   │   │   ├── IDENTITY
                    │   │   │   ├── LOCK
                    │   │   │   ├── LOG
                    │   │   │   ├── MANIFEST-000005
                    │   │   │   └── OPTIONS-000007
                    │   │   ├── payload_storage/
                    │   │   │   ├── bitmask.dat
                    │   │   │   ├── config.json
                    │   │   │   └── gaps.dat
                    │   │   └── vector_storage/
                    │   │       ├── deleted/
                    │   │       │   └── status.dat
                    │   │       └── vectors/
                    │   │           ├── config.json
                    │   │           └── status.dat
                    │   ├── 82c81073-329b-4ec8-b437-1bdcc945f5f7/
                    │   │   ├── segment.json
                    │   │   ├── version.info
                    │   │   ├── payload_index/
                    │   │   │   ├── config.json
                    │   │   │   ├── CURRENT
                    │   │   │   ├── IDENTITY
                    │   │   │   ├── LOCK
                    │   │   │   ├── LOG
                    │   │   │   ├── MANIFEST-000005
                    │   │   │   └── OPTIONS-000007
                    │   │   ├── payload_storage/
                    │   │   │   ├── bitmask.dat
                    │   │   │   ├── config.json
                    │   │   │   └── gaps.dat
                    │   │   └── vector_storage/
                    │   │       ├── deleted/
                    │   │       │   └── status.dat
                    │   │       └── vectors/
                    │   │           ├── config.json
                    │   │           └── status.dat
                    │   ├── 985f9b1c-54cb-4ff9-b629-90b9aeb4d23e/
                    │   │   ├── segment.json
                    │   │   ├── version.info
                    │   │   ├── payload_index/
                    │   │   │   ├── config.json
                    │   │   │   ├── CURRENT
                    │   │   │   ├── IDENTITY
                    │   │   │   ├── LOCK
                    │   │   │   ├── LOG
                    │   │   │   ├── MANIFEST-000005
                    │   │   │   └── OPTIONS-000007
                    │   │   ├── payload_storage/
                    │   │   │   ├── bitmask.dat
                    │   │   │   ├── config.json
                    │   │   │   └── gaps.dat
                    │   │   └── vector_storage/
                    │   │       ├── deleted/
                    │   │       │   └── status.dat
                    │   │       └── vectors/
                    │   │           ├── config.json
                    │   │           └── status.dat
                    │   ├── adf9d829-ad72-4f92-a955-cabd56953dca/
                    │   │   ├── mutable_id_tracker.mappings
                    │   │   ├── mutable_id_tracker.versions
                    │   │   ├── segment.json
                    │   │   ├── version.info
                    │   │   ├── payload_index/
                    │   │   │   ├── config.json
                    │   │   │   ├── CURRENT
                    │   │   │   ├── IDENTITY
                    │   │   │   ├── LOCK
                    │   │   │   ├── LOG
                    │   │   │   ├── MANIFEST-000005
                    │   │   │   └── OPTIONS-000007
                    │   │   ├── payload_storage/
                    │   │   │   ├── bitmask.dat
                    │   │   │   ├── config.json
                    │   │   │   └── gaps.dat
                    │   │   └── vector_storage/
                    │   │       ├── deleted/
                    │   │       │   └── status.dat
                    │   │       └── vectors/
                    │   │           ├── config.json
                    │   │           └── status.dat
                    │   └── c9a83edd-724a-4c31-b4f8-6f2dfb54ddaa/
                    │       ├── segment.json
                    │       ├── version.info
                    │       ├── payload_index/
                    │       │   ├── config.json
                    │       │   ├── CURRENT
                    │       │   ├── IDENTITY
                    │       │   ├── LOCK
                    │       │   ├── LOG
                    │       │   ├── MANIFEST-000005
                    │       │   └── OPTIONS-000007
                    │       ├── payload_storage/
                    │       │   ├── bitmask.dat
                    │       │   ├── config.json
                    │       │   └── gaps.dat
                    │       └── vector_storage/
                    │           ├── deleted/
                    │           │   └── status.dat
                    │           └── vectors/
                    │               ├── config.json
                    │               └── status.dat
                    └── wal/
                        └── first-index



Repository: parrot90/production_ready_rag_ai_agent_in_python
Files analyzed: 110

Estimated tokens: 178.7k


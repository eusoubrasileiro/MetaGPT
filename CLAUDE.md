# MetaGPT Fork — Project Instructions

## What this is
Fork of MetaGPT v0.8.2 (github.com/geekan/MetaGPT) with GPT-5 model support
and cherry-picked upstream fixes. Branch: `feat/gpt5-and-editor-fixes`.

IMPORTANT: We pin to v0.8.2 because upstream `main` was refactored to use
experimental RoleZero/MGXEnv roles that break basic workspace handling.
v0.8.2 is the last stable release with the documented working flow.

## How MetaGPT works — DO NOT fight this

- `generate_repo(idea, project_name="x")` is the entry point
- Output goes to `workspace/x/` — this is by design
- `PrepareDocuments` action initializes the project folder
- `WritePRD` writes the PRD to `workspace/x/docs/prd/`
- Human questions are prompted in the terminal — that's the UX
- `config/config2.yaml` controls model, API keys, workspace path

## DO NOT
- Modify MetaGPT source to fix problems before checking the official docs
- Monkey-patch MetaGPT internals (ProductManager, WritePRD, etc.)
- Hardcode absolute paths in IDEA prompts
- Auto-answer human questions with set_human_input_func
- Create custom output directories that bypass workspace/
- Rename upstream parameter names (filename, file_name) — makes merges harder
- Rebase onto upstream `main` — it has breaking changes (MGXEnv, RoleZero)

## Running
Script: .venv/bin/python run_optizap.py

After: cp -r workspace/optizap output/optizap_<model>_runN

## Config
- Model: config/config2.yaml -> llm.model
- Budget: generate_repo(investment=N) — dollar cap
- Rounds: generate_repo(n_round=N) — 5=quick, 20=thorough
- Architecture only: implement=False, code_review=False, run_tests=False

## Our changes vs upstream v0.8.2
- GPT-5 support: constant.py, token_counter.py, action_node.py, role.py
- ToT security fix eval->json.loads (PR #1946): tot.py

## Upstream PRs to watch
- #1883 (GPT-5 full) — we cherry-picked what we need
- #1946 (ToT security) — cherry-picked
- #1950 (bare except cleanup) — nice to have, not critical

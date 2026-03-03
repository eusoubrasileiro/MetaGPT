"""Run MetaGPT to produce architecture for OptiZap WhatsApp AI bot.

Script usage:
    .venv/bin/python run_optizap.py

Output: workspace/optizap/
Save results: cp -r workspace/optizap output/optizap_<model>_runN
"""

from metagpt.software_company import generate_repo

IDEA = """
Design a complete, production-ready architecture for a WhatsApp AI chatbot for an optical store chain in Brazil (OptiZap).

CRITICAL: This is an ARCHITECTURE-ONLY project. Do NOT produce any code files (.ts, .js, .prisma, etc).
Only produce design documents in Markdown format.

IMPORTANT: Write ALL documents in ENGLISH.
Only use Brazilian Portuguese for example user-facing bot messages and sample utterances in the NLU dataset.

## BUSINESS REQUIREMENTS

The bot handles pre-service triage: understanding what the customer needs, collecting required information, and either resolving their query directly or handing off to a human specialist with full context.
HARD REQUIREMENT FROM PO: The bot MUST sound like a real human, NEVER like a bot. No robotic templates, no "Dear customer", no numbered menus. Responses must feel like texting a friendly store employee. This is a non-negotiable UX requirement.
The bot should handle the 7 customer needs below but soon more needs will arise.

### Customer Needs (7 observed patterns)

| # | Customer Need | What it does | Data to collect | Resolution |
|---|--------|-------------|-----------------|------------|
| 1 | Prescription glasses purchase | Customer wants to buy prescription glasses | Name, prescription status (has/doesn't have), prescription file (photo/PDF, conditional on having one), style preference (optional) | Hand off to human optician with all collected data |
| 2 | Sunglasses purchase | Customer wants sunglasses | Name, style preference (optional) | Hand off to human with collected data |
| 3 | Contact lenses purchase | Customer wants contact lenses | Name, prescription status, prescription file (conditional) | Hand off to human with collected data |
| 4 | Order status inquiry | Customer wants to check their order | Order number OR CPF (Brazilian tax ID) — either one works | Look up in database, return status |
| 5 | Store hours & address | Customer asks when the store is open or where it is | Nothing — answer is in the database | Return store info from DB |
| 6 | Schedule eye exam | Customer wants to book an eye exam appointment | Name | Currently: hand off to human. FUTURE: check Google Calendar availability, suggest times, book slot |
| 7 | General / other | Not specified yet may change | Nothing | Free-form conversational response |

### Special cases:
- Explicit "talk to human" request → immediate handoff regardless of context
- Angry customer (detected) → immediate handoff
- Multi-need messages: customer says "Quero óculos de grau e qual o horário de vocês?" (prescription glasses + store hours in one message) → bot should handle both
- Outside business hours: bot still responds but adds a notice that humans are unavailable until next business day

### Hard Technical Constraints
- Language: TypeScript monorepo (backend: Hono web framework, frontend: React + Vite)
- Pipeline orchestration: LangGraph (TypeScript, v1.0+)
- Messaging: WhatsApp Cloud API (Meta)
- Database: PostgreSQL via Prisma ORM
- Team size: Solo developer. The architecture must be maintainable by ONE person.
- Language: All user-facing text in Brazilian Portuguese
- LLM providers: OpenAI (gpt-4.1, gpt-4.1-mini), Google (Gemini Flash), Groq — can use different models for different tasks
- Latency: Sub-10 second end-to-end response time (WhatsApp UX constraint)
- Tone: ALL bot responses MUST sound natural and human — like a friendly store employee texting back. NEVER use robotic templates, canned greetings ("Dear customer"), numbered option menus, or formulaic patterns. The architecture must ensure LLM-generated free-form responses for every interaction, not template-based routing.

### Required Outputs (DOCUMENTS ONLY — NO CODE)
1. PRD (product requirements document)
2. Full architecture document
3. Full pipeline graph: every node, every edge, every conditional branch
4. LangGraph state management design (schemas, lifecycle, persistence)
5. Customer need handling flows (all 7 + special cases)
6. NLU schema with intents, entities, slots
7. Sample utterance dataset (CSV)
8. Future-proofing: Google Calendar integration path
9. Testing strategy document
"""

repo = generate_repo(
    idea=IDEA,
    investment=2.0,
    n_round=5,
    code_review=False,
    run_tests=False,
    implement=False,
    project_name="optizap",
)

print(f"\nOutput at: {repo.workdir}")

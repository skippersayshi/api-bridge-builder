# API Bridge Builder

Autonomous API connection generator with natural language input, SQLite knowledge base, and Ralph loop.

## What it does

- Parses plain language descriptions into structured mapping intents (via Claude Haiku)
- Generates field mappings between source and target systems autonomously
- Tests structural validity of each mapping
- Stores results in SQLite — reuses successful mappings on future runs
- Ralph loop: refines using prior knowledge, gets smarter with every run

## Install

```bash
pip install anthropic httpx pydantic
export ANTHROPIC_API_KEY=your_key
```

## Run

```bash
python bridge_builder.py
```

## Components

| Class | Role |
|---|---|
| `NLParser` | Plain language -> MappingIntent via Claude |
| `BridgeBuilder` | Generates field mappings via Claude |
| `ConnectionTester` | Validates mapping structure |
| `KnowledgeBase` | SQLite cache + learning store |
| `RalphLoop` | Orchestrates full autonomous cycle |

## Example

```python
loop = RalphLoop()
result = loop.run("Connect Salesforce to SAP via REST. Map customer_id, email, invoice_total.")
```

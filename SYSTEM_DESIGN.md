# System Design — AI Front-Desk Voice Assistant

## 1) Architecture Overview

**Goal:** Automate front-office tasks (scheduling, simple insurance verification, FAQs) through a voice assistant.

**Flow**
1. Caller speaks → VAPI captures audio
2. STT (in VAPI) → transcribes to text
3. LLM (in VAPI) → interprets intent and decides next step
4. If action needed → VAPI calls FastAPI tools:
   - `POST /schedule`
   - `POST /verify_insurance`
   - `GET /faq?question=...`
5. FastAPI returns JSON → LLM composes a concise reply
6. TTS (in VAPI) → speaks the reply back to the caller

**Components**
- **VAPI Assistant**: Orchestration (STT/LLM/TTS), tool-calling, turn-taking
- **FastAPI Backend**: Stateless endpoints with mocked business logic
- **Railway**: Public hosting for the API
- **Client**: VAPI console/web widget/phone number

---

## 2) Tech Stack & Tools

- **FastAPI + Uvicorn + Pydantic**: Lightweight Python API with typed models
- **VAPI**: Real-time voice pipeline (STT/TTS/LLM) and API tool integration
- **Railway**: One-click deploy + public domain for the backend
- **Python 3.10+**

**Why**
- FastAPI provides speed, readability, and auto-generated docs at `/docs`
- VAPI simplifies real-time voice, latency, and dialogue control
- Railway ensures a reproducible, public endpoint without infra overhead

**Pluggable Choices**
- STT/TTS providers (OpenAI, Azure, Google, ElevenLabs, etc.)
- LLM provider (configurable in VAPI)
- These can be swapped without changing the API surface

---

## 3) Prompt Engineering

**Objectives**
- One question at a time; avoid repetition and filler
- Concise, friendly, professional responses
- Cover **three** capabilities: Scheduling, Insurance, FAQs
- Short confirmations and quick closure if user is impatient

**Key Strategies**
- Strong identity/scope in the system prompt
- Grouped data collection (e.g., name/DOB/phone) when appropriate
- If slot unavailable → offer 1–2 alternatives, then move on
- Answer FAQs directly and end unless the user asks for more

**Example Behaviors**
- Hours/location questions → single, crisp answer + optional “anything else?”
- Booking → gather essentials → confirm once → provide prep instructions
- Insurance → accepted list (Aetna, Blue Cross, Cigna, United Health); otherwise suggest front-desk verification

---

## 4) Backend Logic (Mocked)

- **`POST /schedule`**
  - Request: `{name, date, time}`
  - Response: confirmation string
- **`POST /verify_insurance`**
  - Request: `{name, provider, procedure}`
  - Response: accepted/not-accepted message (against a small whitelist)
- **`GET /faq?question=hours|location|parking|contact`**
  - Response: canned, concise answers

Notes:
- No persistence; purely stateless and deterministic for easy testing
- In production, replace mocks with real integrations (calendar, eligibility, EHR)

---

## 5) Assumptions & Limitations

**Assumptions**
- Single speaker, US English
- Dates provided clearly or clarified by the assistant
- No PHI persisted; demo context only

**Limitations**
- No real calendar/eligibility/EHR integrations
- Minimal error handling (sufficient for prototype)
- No HIPAA storage/logging/BAA in this demo

**Improvements (Future Work)**
- Real scheduling (Google/Office, EHR)
- Eligibility via clearinghouse APIs
- Analytics, retries/backoff, quality metrics
- Human handoff with transcript/context
- HIPAA compliance (encrypted storage, RBAC, audit trails)

---

## 6) Test Plan & Demos

**Happy Path — Appointment**
- User asks for a primary care visit with Dr. Lee on Monday
- Assistant groups info (name/DOB/phone), offers earliest slot, confirms once
- Saved as `demos/call1_appointment.mp3`

**Edge Case — Insurance**
- User asks if a non-whitelisted provider is accepted
- Assistant responds gracefully, suggests front-desk verification
- Also answers a quick FAQ (hours/location)
- Saved as `demos/call2_insurance_edgecase.mp3`

**FAQ Quick Check**
- Hours/location/parking/contact return concise answers
- Assistant does not repeat identity; minimal follow-up

---

## 7) Deployment Notes

- **Procfile**: `web: uvicorn main:app --host 0.0.0.0 --port 8000`
- **Requirements**: `fastapi`, `uvicorn`, `pydantic`
- **CORS**: enabled for VAPI calls
- **Docs**: available at `/docs` on your Railway domain

---

## 8) Diagram (Text)

# AI Front-Desk Voice Assistant — Confido Health Take-Home

## 📁 Repository Contents
- **main.py** – Core FastAPI backend handling scheduling, insurance, and FAQ routes  
- **requirements.txt** – Python dependencies for local setup  
- **Procfile** – Command used for deployment on Railway  
- **README.md** – Setup and usage instructions  
- **SYSTEM_DESIGN.md** – Explanation of architecture, tech stack, and prompt design  

This project is a prototype AI front-desk assistant for healthcare admin tasks.  
It supports **appointment scheduling**, **insurance verification**, and **clinic FAQs**, and is integrated with a **voice assistant (VAPI)** for real-time, spoken interactions.

## Live Demo (API)
Base URL: https://YOUR-RAILWAY-DOMAIN.up.railway.app  
Interactive API docs: https://YOUR-RAILWAY-DOMAIN.up.railway.app/docs

> Replace the domain above with your Railway public domain.

---

## Features
- Appointment booking via `/schedule`
- Insurance verification via `/verify_insurance`
- Clinic FAQs via `/faq`
- Deployed on Railway (publicly reachable)
- Voice assistant integration via VAPI (speech-to-text, LLM, text-to-speech)

---

## Tech Stack
- **Backend:** FastAPI (Python)
- **Voice/Orchestration:** VAPI (configurable STT/TTS + LLM)
- **Hosting:** Railway
- **Python:** 3.10+

---

## Endpoints

| Endpoint            | Method | Description                              |
|--------------------|--------|------------------------------------------|
| `/`                | GET    | Health check                             |
| `/schedule`        | POST   | Books an appointment                     |
| `/verify_insurance`| POST   | Verifies provider acceptance (mocked)    |
| `/faq`             | GET    | Answers clinic FAQs (hours/location/etc) |

### Request / Response Examples

**Health Check**

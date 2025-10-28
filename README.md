# AI Front-Desk Voice Assistant — Confido Health Take-Home

This project demonstrates a prototype AI voice assistant for healthcare front-office automation.  
It handles appointment scheduling, insurance verification, and FAQs using Generative AI and Voice AI.

## 🚀 Features
- Appointment booking via `/schedule`
- Insurance verification via `/verify_insurance`
- Clinic FAQs via `/faq`
- Deployed on **Railway**
- Integrated with **VAPI** for real-time voice interaction

## 🧠 Tech Stack
- FastAPI (backend API)
- Python 3.10
- OpenAI/VAPI for conversational intelligence
- Railway for cloud hosting
- JSON-based simulation (no real integrations)

## 🧩 Endpoints
| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/` | GET | Health check |
| `/schedule` | POST | Books appointments |
| `/verify_insurance` | POST | Verifies insurance provider |
| `/faq` | GET | Answers clinic FAQs |

## 💻 How to Run Locally
```bash
git clone <repo-url>
cd <repo-folder>
pip install -r requirements.txt
uvicorn main:app --reload

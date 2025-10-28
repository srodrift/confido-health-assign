from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# --- Root Route ---
@app.get("/")
def read_root():
    return {"message": "Health Voice AI backend is live and running!"}

# --- Appointment Scheduling ---
class Appointment(BaseModel):
    name: str
    date: str
    time: str

@app.post("/schedule")
def schedule_appointment(appt: Appointment):
    return {
        "confirmation": f"Appointment booked for {appt.name} on {appt.date} at {appt.time}."
    }

# --- Insurance Verification ---
class InsuranceCheck(BaseModel):
    name: str
    provider: str
    procedure: str

@app.post("/verify_insurance")
def verify_insurance(details: InsuranceCheck):
    accepted_insurances = ["Aetna", "Blue Cross", "Cigna", "United Health"]
    if details.provider in accepted_insurances:
        return {
            "verification": f"Yes, {details.provider} is accepted for {details.procedure}. Coverage verified for {details.name}."
        }
    else:
        return {
            "verification": f"Unfortunately, {details.provider} is not in our accepted list. Please contact our front desk for assistance."
        }

# --- FAQs about the Clinic ---
@app.get("/faq")
def clinic_faq(question: str):
    faq_data = {
        "hours": "We’re open Monday through Friday from 8 AM to 5 PM, and Saturday from 9 AM to 12 PM.",
        "location": "We’re located at 123 Wellness Street, San Francisco, CA.",
        "parking": "Free parking is available in the rear lot behind the building.",
        "contact": "You can reach us at (415) 555-0199 or info@wellnesspartners.com.",
    }
    answer = faq_data.get(
        question.lower(),
        "I’m sorry, I don’t have that information. Please check our website or contact our office."
    )
    return {"answer": answer}

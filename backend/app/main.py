from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Ethical Decision Simulator API")

class Scenario(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Ethical Decision Simulator API is live 🚀"}

@app.post("/predict")
def predict(scenario: Scenario):
    # Placeholder until we connect the ML model
    return {"decision": "ambiguous", "explanation": "Model not trained yet"}

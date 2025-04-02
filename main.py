from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="ELI5",
    version="1.0",
    description="ELI5 (Explain Like Im 5) is an AI-powered learning assistant designed to help users deeply understand complex topics by breaking them down and explaining them in their own words. Inspired by the Feynman Technique, this API challenges users with thought-provoking hints rather than direct corrections, fostering critical thinking and reinforcing comprehension through an iterative learning process."
)

# Include all routes from router
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Hi, I am ELIS. Lets study together"}
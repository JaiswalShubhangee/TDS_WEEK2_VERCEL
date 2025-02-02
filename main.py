from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS to allow GET requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data from JSON file
with open("data.json", "r") as file:
    students = json.load(file)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/api")
def get_marks(name: list[str]):
    marks = [next((s["marks"] for s in students if s["name"] == n), None) for n in name]
    return {"marks": marks}

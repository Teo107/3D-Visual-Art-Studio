from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models, database

# This line is the "Magic" — it creates the tables in Postgres automatically
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="3D Visual Art Studio")

# Configure CORS
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "3D Visual Art Studio API is Online"}
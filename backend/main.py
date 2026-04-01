from fastapi import FastAPI
import models, database

# This line is the "Magic" — it creates the tables in Postgres automatically
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="3D Visual Art Studio")

@app.get("/")
def home():
    return {"status": "3D Visual Art Studio API is Online"}
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from settings.database import engine
from snapfaceapi import model
from snapfaceapi.route import app_facesnap

app = FastAPI()
app.include_router(app_facesnap)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Origines autorisées
    allow_credentials=True,
    allow_methods=["*"],  # Permet toutes les méthodes HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permet tous les en-têtes
)
model.Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="127.0.0.1", port=8000, reload=True)

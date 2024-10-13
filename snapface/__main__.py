from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status
import uvicorn
from settings.secret import authentication
from settings.database import engine
from snapfaceapi import model


app = FastAPI()


model.Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="127.0.0.1", port=8000, reload=True)

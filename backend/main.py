import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Database import engine
import models
import crud
import auth

app = FastAPI(title="Uptemoll",
              version='0.1.0',
              docs_url="/")
models.Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
app.include_router(crud.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # allow all origins
    allow_credentials=True,
    allow_methods=["*"], # allow all HTTP methods
    allow_headers=["*"], # allow all headers
)


from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session
from dependencies import get_db_session
import uvicorn
import os

load_dotenv()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Cooking Book API",
        version="0.0.1",
        description="This is the API for the Cooking Book project. It allows you to interact with the recipes and ingredients.",
        routes=app.routes,
        servers=[{
            "url":"/api"
        }]
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app = FastAPI(root_path="/api")
app.openapi = custom_openapi


origins = ["http://localhost:8080"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/init_db')
def init_db(db_session: Session = Depends(get_db_session)):
    with open("init_db.sql") as f:
        query = text(f.read())
        db_session.execute(query)
    return "Database initialized"


if __name__ == "__main__":
    uvicorn.run("app:app",
                host="localhost",
                port=5000,
                reload=True)
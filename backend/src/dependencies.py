import os
from typing import Generator
from models.secrets_parser import SecretsParser
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()



secrets = SecretsParser(
    DB_PATH=os.getenv("DB_PATH",None),
)


def get_secrets() -> SecretsParser:
    return secrets


def get_db_session() -> Generator[Session,None,None]:
    engine = create_engine(secrets.DB_URL)
    db_session_maker = sessionmaker(bind=engine)
    session = db_session_maker()
    try:
        yield session
    finally:
        session.close()
        engine.dispose()
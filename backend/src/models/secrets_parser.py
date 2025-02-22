from pydantic import BaseModel

class SecretsParser(BaseModel):
    DB_PATH: str

    @property
    def DB_URL(self):
        return f"sqlite:///{self.DB_PATH}"
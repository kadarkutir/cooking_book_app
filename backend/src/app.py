from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn
import os

load_dotenv()

app = FastAPI()


DAILY_MESSAGE = os.getenv("DAILY_MESSAGE_FROM_NAGY_MARK",None)


@app.get("/get_nagy_mark")
def get_nagy_mark(): 
    return {"message": DAILY_MESSAGE}


if __name__ == "__main__":
    uvicorn.run("app:app",
                host="localhost",
                port=5000,
                reload=True)
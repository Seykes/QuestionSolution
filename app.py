import uvicorn
from fastapi import FastAPI

from src.words import most_common_words

app = FastAPI()

@app.get("/words")
def read_root():
    words = most_common_words()
    dictList = list({word:count} for word,count in words)

    return {"words": dictList}


if __name__ == "__main__":
    uvicorn.run(app, port=9090)
import uvicorn
from fastapi import FastAPI

from src.api.route import developer_test


app = FastAPI()
app.include_router(developer_test)


@app.get("/")
def root():
    return {"message": "Hello I'am ready!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000)
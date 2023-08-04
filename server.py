import uvicorn
from fastapi import FastAPI

from api.routers import router as api_router

app = FastAPI()
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("server:app", reload=True, port=4000)

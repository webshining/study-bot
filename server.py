import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.routers import router as api_router

origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://localhost",
    "https://localhost:3000",
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("server:app", reload=True, port=4000, host="0.0.0.0")

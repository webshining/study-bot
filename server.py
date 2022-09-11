import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api import subjectsRouter


app = FastAPI()
app.include_router(subjectsRouter)
origins = [
    "http://localhost:3000",
    "https://react-dashboard-black.vercel.app"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=['https://react-dashboard-black.vercel.app/'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

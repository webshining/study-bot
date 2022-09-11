import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api import subjectsRouter


app = FastAPI()
app.include_router(subjectsRouter)
origins = [
    "https://react-dashboard-black.vercel.app"
]
app.add_middleware(
    CORSMiddleware,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
async def root_router():
    return {'status': 'Aboba'}

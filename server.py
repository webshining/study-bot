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
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


if __name__ == '__main__':
    uvicorn.run('server:app', reload=True, host='0.0.0.0', port=4000)

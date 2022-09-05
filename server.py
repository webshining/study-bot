import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api import usersRouter, subjectsRouter, daysRouter

app = FastAPI()
app.include_router(prefix='/api', router=usersRouter)
app.include_router(prefix='/api', router=subjectsRouter)
app.include_router(prefix='/api', router=daysRouter)
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run('server:app', reload=True, host='0.0.0.0', port=4000)

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api.routes import SubjectRouter, UserRouter

app = FastAPI(title="WebShining Study Bot")
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
app.include_router(SubjectRouter, prefix='/api/v1/subjects')
app.include_router(UserRouter, prefix='/api/v1/users')


if __name__ == '__main__':
    uvicorn.run('server:app', host='0.0.0.0', port=4000, reload=True)
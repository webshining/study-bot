import uvicorn
from fastapi import FastAPI
from api import usersRouter, subjectsRouter, daysRouter

app = FastAPI()
app.include_router(prefix='/api', router=usersRouter)
app.include_router(prefix='/api', router=subjectsRouter)
app.include_router(prefix='/api', router=daysRouter)

if __name__ == '__main__':
    uvicorn.run('server:app', reload=True, host='0.0.0.0', port=8000)

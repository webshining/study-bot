import uvicorn
from fastapi import FastAPI

from api import routes

app = FastAPI()
app.include_router(routes.days_router)
app.include_router(routes.subjects_router)


if __name__ == '__main__':
    uvicorn.run('server:app', host='0.0.0.0', port=4000, reload=True)
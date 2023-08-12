from fastapi import APIRouter, Depends

from api.services import get_current_user

from .auth import router as auth_router
from .subjects import router as subjects_router
from .users import router as users_router

router = APIRouter(prefix='/api')

authorized_router = APIRouter(dependencies=[Depends(get_current_user)])

unauthorized_router = APIRouter()
unauthorized_router.include_router(auth_router, prefix='/auth')
unauthorized_router.include_router(users_router, prefix='/users')
unauthorized_router.include_router(subjects_router, prefix='/subjects')

router.include_router(unauthorized_router)
router.include_router(authorized_router)
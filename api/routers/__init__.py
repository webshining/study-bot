from fastapi import APIRouter

from .auth import router as auth_router
from .subjects import router as subjects_router
from .users import router as users_router

router = APIRouter(prefix='/api')
router.include_router(auth_router, prefix='/auth')
router.include_router(users_router, prefix='/users')
router.include_router(subjects_router, prefix='/subjects')

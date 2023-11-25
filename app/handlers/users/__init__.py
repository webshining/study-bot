from .call_schedule import router
from .current_lesson import router
from .inline import router
from .openai import router
from .schedule import router
from .select_group import router
from .start import router
from .tasks import router

__all__ = ['router']

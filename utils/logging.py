from pathlib import Path
from loguru import logger

logger.add(f'{Path(__file__).absolute().parent.parent}/logs/log.out', format="[{time}]-[{level}]-[{message}]", rotation="1 day")

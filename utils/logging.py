from pathlib import Path
from loguru import logger

logger.add(f'{Path(__file__).absolute().parent.parent}/data/logs/log.out', format='[{level}]-[{time}]', rotation='1 day')

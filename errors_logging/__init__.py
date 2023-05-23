from loguru import logger
from . import settings
from typing import NoReturn


def logger_init() -> NoReturn:
	for level in settings.LOGGING_LEVELS:
		logger.add(
			settings.ERRORS_OUTPUT_FILE,
			level=level,
			format=settings.LOGGING_FORMAT,
			rotation="10 KB",
			compression="zip"
		)

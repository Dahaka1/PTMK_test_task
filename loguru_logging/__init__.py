from loguru import logger
from . import settings
from typing import Optional
import time


def logger_init() -> None:
	for level in settings.LOGGING_LEVELS:
		logger.add(
			settings.ERRORS_OUTPUT_FILE,
			level=level,
			format=settings.LOGGING_FORMAT,
			rotation="1 MB",
			compression="zip"
		)


def log_func_error(exception: Optional[Exception] = None) -> None:
	logger.error(
		f'Function working error. {"Exception content: " + str(exception) if not exception is None else ""}'
	)


def successfully(func) -> float:
	end_time = time.monotonic()
	logger.info(f"{func.__doc__.strip()} ('{func.__name__}') successfully completed!")
	return end_time


def starting(func) -> None:
	logger.info(f"{func.__doc__.strip()} ('{func.__name__}') starting...")


def closing_info() -> None:
	logger.info(
		"Press Ctrl+C to exit process early than it's closing"
	)

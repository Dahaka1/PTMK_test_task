from typing import Callable
import time
from loguru import logger
import errors_logging


def handle_func(foo: Callable) -> Callable:
	handle_func.__doc__ = foo.__doc__

	def _wrapper(*args):
		start_time = time.monotonic()
		errors_logging.starting(foo)
		try:
			foo(*args)
		except Exception as exception:
			errors_logging.log_func_error(handle_func, exception)
		else:
			end_time = errors_logging.successfully(foo)
			logger.info(
				f"{foo.__doc__.strip()} ('{foo.__name__}') working took {end_time - start_time} sec."
			)
	func = _wrapper
	func.__name__ = foo.__name__
	return func


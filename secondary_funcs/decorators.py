from typing import Callable
import time
from loguru import logger
import loguru_logging
from main_funcs.other import get_advanced_results


def handle_func(foo: Callable) -> Callable:
	handle_func.__doc__ = foo.__doc__

	def _wrapper(*args):
		start_time = time.monotonic()
		loguru_logging.starting(foo)
		try:
			foo(*args)
		except Exception as exception:
			loguru_logging.log_func_error(handle_func, exception)
		else:
			end_time = loguru_logging.successfully(foo)
			if foo.__doc__ in ['func number 5', 'func number 6']:
				get_advanced_results(end_time, foo.__doc__[-1])
			logger.info(
				f"{foo.__doc__.strip()} ('{foo.__name__}') working took {end_time - start_time} sec."
			)
	func = _wrapper
	func.__name__ = foo.__name__
	return func

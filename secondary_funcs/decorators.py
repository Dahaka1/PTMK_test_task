from typing import Callable
import time
from loguru import logger
import loguru_logging
from secondary_funcs.queries import get_advanced_results
from secondary_funcs.represent import get_results


def handle_func(foo: Callable) -> Callable:
	handle_func.__doc__ = foo.__doc__

	def _wrapper(*args, **kwargs):
		start_time = time.monotonic()
		loguru_logging.starting(foo)
		try:
			foo(*args)
		except Exception as exception:
			loguru_logging.log_func_error(exception)
		else:
			end_time = loguru_logging.successfully(foo)
			result = end_time - start_time
			try:
				foo.__doc__ = kwargs['current_func'].__doc__
			except:
				pass
			if foo.__doc__.strip() in ['func number 5', 'func number 6']:
				get_advanced_results(result, foo.__doc__.strip()[-1])
			logger.info(
				f"{foo.__doc__.strip()} ('{foo.__name__}') working took {result} sec."
			)
			if foo.__doc__.strip() == 'func number 6':
				get_results()
	func = _wrapper
	func.__name__ = foo.__name__
	return func

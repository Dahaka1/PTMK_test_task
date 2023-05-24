from loguru import logger
from .settings import get_func_by_command
from . import commands_handling
from secondary_funcs import cmd_args_exists
from . import strings
from tests.test_start import test_cmd_args
from secondary_funcs.represent import get_logs


def execute_from_command_line(args):
	try:
		test_cmd_args(args)
	except Exception as exception:
		logger.error(
			f"Getting command line arg error: {exception.__class__.__name__} - {exception}"
		)
	else:
		main_arg = args[1]
		if main_arg != 'log':
			func_num = int(args[1])
			func = get_func_by_command[func_num]
			func_args = args[2:] if cmd_args_exists() else None
			try:
				func = getattr(commands_handling, func)
				func(func_args) if func_args is not None else func()
			except Exception as exception:
				logger.error(
					exception
				)
		else:
			get_logs()

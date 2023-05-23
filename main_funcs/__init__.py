from loguru import logger
from .settings import get_func_by_command
from . import commands_handling
from secondary_funcs import cmd_args_exists
from . import strings


def execute_from_command_line(args):
	try:
		func_num = int(args[1])
	except Exception as exception:
		logger.error(
			f"Getting command line arg error: {exception.__class__.__name__}"
		)
	else:
		func = get_func_by_command[func_num]
		func_args = args[2:] if cmd_args_exists() else None
		try:
			func = getattr(commands_handling, func)
			func(func_args) if func_args is not None else func()
		except Exception as exception:
			logger.error(
				exception
			)


def sql():
	return strings.sql

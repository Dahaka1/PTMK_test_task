from typing import Callable
import main_funcs
import sys


def sql(foo: Callable) -> str:
	return main_funcs.sql()[foo.__name__]


def cmd_args_exists() -> bool:
	if len(sys.argv) > 2:
		return True
	return False

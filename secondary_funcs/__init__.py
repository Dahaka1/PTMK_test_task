from __future__ import annotations

from typing import Callable
import main_funcs.strings
import sys


def sql(arg: Callable | str) -> str:
	if isinstance(arg, Callable):
		func = arg.__name__
	elif isinstance(arg, str):
		func = arg
	return main_funcs.strings.sql[func]


def cmd_args_exists() -> bool:
	if len(sys.argv) > 2:
		return True
	return False

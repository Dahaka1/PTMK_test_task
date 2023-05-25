from typing import Iterable, Sized, Union
import json
from secondary_funcs.queries import get_table_count
from loguru import logger


def write_to_console_unique_persons(persons_list: map, pk=False) -> None:
	if not pk:
		print(*[person for person in persons_list], sep='\n')
	else:
		print(*[f'{person.pk} + {person}' for person in persons_list], sep='\n')


def get_args(args: Union[Sized, Iterable]) -> None:
	print(*args, sep='\n')
	logger.info(
		f"FUNCTION #5: {len(args)} rows was turned out from {get_table_count()} line."
	)


def get_logs() -> None:
	with open('loguru_logging/logs.log', encoding='utf-8') as file:
		logs_list = file.read()
		print(logs_list)


def get_results() -> None:
	"""
	for func number 6
	"""
	file_path = 'tests/timing_results.json'
	try:
		results: dict = json.load(open(file_path))
		out = '\n'.join(f"{i}: {j}" for i, j in results.items())
		print(f"RESULTS:\n{out}")
	except FileNotFoundError:
		raise FileNotFoundError("There is no fixed by func number 5 results in timing_results.json")

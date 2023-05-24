from typing import Iterable
import json


def write_to_console_unique_persons(persons_list: map, pk=False) -> None:
	if not pk:
		print(*[person for person in persons_list], sep='\n')
	else:
		print(*[f'{person.pk} + {person}' for person in persons_list], sep='\n')


def get_args(args: Iterable[Iterable]) -> None:
	print(*args, sep='\n')


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
		results = json.load(open(file_path))
	except FileNotFoundError:
		raise FileNotFoundError("There is no fixed by func number 5 results in timing_results.json")
	print(results)

from database import conn
from typing import Callable, Iterable
from secondary_funcs import sql
from main_funcs.strings import get_db_table_length, get_person
import json
from loguru import logger


def execute_all(foo: Callable, args: Iterable):
	if foo.__name__ == 'post_advanced':
		query = sql("post")
		with conn.cursor() as cursor:
			for person in args:
				params = person.fullname, person.birthdate, person.sex
				cursor.execute(query, params)


def get_advanced_results(time: float, func_num: str) -> None:
	"""
	for funcs number 5 and 6
	"""
	file_path = 'tests/timing_results.json'
	try:
		results_output = json.load(open(file_path))
	except FileNotFoundError:
		results_output = {}
	json_dict = {
		"5": "BEFORE_OPTIMIZING_DB",
		"6": "AFTER_OPTIMIZING_DB"
	}
	results_output[json_dict[func_num]] = {
		"FUNC_WORKING_TIME": time
	}
	json.dump(results_output, open(file_path, 'w'), indent='\t')
	logger.info(
		f"Function #{func_num} working results was fixed in 'tests/timing_results.json'"
	)


def get_person_id_and_sex(person) -> tuple[int, str]:
	with conn.cursor() as cursor:
		cursor.execute(get_person, (person.fullname, person.birthdate))
		pk, sex = cursor.fetchone()
	return pk, sex


def get_table_count():
	with conn.cursor() as cursor:
		cursor.execute(get_db_table_length)
		return cursor.fetchone()[0]

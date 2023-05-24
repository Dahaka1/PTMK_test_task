from loguru import logger
from .strings import get_db_table_length
from database import conn
import json


def get_sex_choices(lang_code: str) -> list[str]:
	if lang_code == 'ru':
		return ['мужчина', 'женщина']
	elif lang_code == 'en':
		return ['male', 'female']
	else:
		logger.error(
			"Chosen language code in settings.py must be in ('en', 'ru')"
		)


def get_advanced_results(time: float, func_num: str) -> None:
	"""
	for func number 5 and 6
	"""
	with conn.cursor() as cursor:
		cursor.execute(get_db_table_length)
	table_rows_amount = cursor.fetchone()[0]
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
	results_output["TABLE_STRINGS_AMOUNT"] = table_rows_amount
	json.dump(results_output, open(file_path, 'w'), indent='\t')
from __future__ import annotations
from typing import NamedTuple, Callable
from datetime import date
from tests.test_post import test_format_args
from loguru import logger
from main_funcs.settings import language_code, sex_choices
import names
import random


class FormattedArgsPost(NamedTuple):
	"""
	func "post"
	"""
	fullname: str
	birthdate: date
	sex: str


def format_args(args: list, foo: Callable | str) -> FormattedArgsPost:
	"""
	supported funcs: post, ...
	"""
	current_function = foo if isinstance(foo, str) else foo.__name__
	if current_function == "post":
		fullname = ' '.join(args[:3])
		birthdate = args[3]
		sex = args[4]

		args = test_format_args(fullname, birthdate, sex)

		return FormattedArgsPost(*args)

	else:
		raise AttributeError(f"Function named '{foo.__name__}' wasn't found")


def formatted_date(birthdate: date):
	return birthdate.strftime('%d.%m.%Y')


def generate_person_params(firstname: str = None) -> tuple[str, date, str]:
	if language_code == 'en':
		sex = random.choice(sex_choices)
		if firstname is None:
			fullname = names.get_full_name(sex)
		else:
			fullname = firstname + names.get_last_name()
		randdate_ordinal = random.randrange(708000, 738000)
		birthdate = date.fromordinal(randdate_ordinal)
		return fullname, birthdate, sex
	elif language_code == 'ru':  # если будет нужно, добавить можно генерацию русских имен
		logger.error(
			"Generating of russian names doesn't supports"
		)


def generate_person_started_with_F() -> tuple[str, date, str]:
	with open('static/first_names_starts_with_F.txt', encoding='utf-8') as names_file:
		names_starts_with_f = names_file.readlines()
	random_name = random.choice(names_starts_with_f).rstrip()
	return generate_person_params(firstname=random_name)

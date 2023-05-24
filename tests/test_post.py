from secondary_funcs.strings import fullname_regex, birthdate_regex
from main_funcs.settings import sex_choices
from datetime import date, datetime
import re
from main_funcs.settings import language_code
from loguru import logger


def test_format_args(*args):
	fullname, birthdate, sex = args
	if language_code == 'ru':
		fullname_example = 'Иванов Иван Иванович'
	elif language_code == 'en':
		fullname_example = 'Ivanov Ivan Ivanovich'
	else:
		logger.error(
			"Chosen language code in settings.py must be in ('en', 'ru')"
		)
	assert re.match(fullname_regex, fullname), f"Got an invalid fullname. It must be like '{fullname_example}'"

	assert re.match(birthdate_regex, birthdate), \
		"Format of birthdate-string isn't valid. It must be like 'dd.mm.yyyy'"

	birthdate = datetime.strptime(birthdate, "%d.%m.%Y").date()

	assert date.today().year - birthdate.year < 100, "Got an invalid birthdate. " + \
													 "It must be later than 100 years from today."

	assert sex in sex_choices, f"Got an invalid sex param. It must be {' or '.join(sex_choices)}"

	return fullname, birthdate, sex

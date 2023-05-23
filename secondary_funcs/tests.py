from typing import Callable
from .strings import birthdate_regex, fullname_regex
import re
from main_funcs.settings import sex_choices


def test_args_list(foo: Callable, args: list) -> None:
	if foo.__name__ == 'post':
		fullname, birthdate, sex = args

		assert re.match(fullname_regex, fullname), "Got an invalid fullname. It must be like " \
												   "'Иванов Иван Иванович' or 'Ivanov Ivan Ivanovich'"

		assert re.match(birthdate_regex, birthdate), \
			"Format of birthdate-string isn't valid. It must be like 'dd.mm.yyyy'"

		assert sex in sex_choices, f"Got an invalid sex param. It must be {' or '.join(sex_choices)}"


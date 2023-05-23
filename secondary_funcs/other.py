from typing import NamedTuple, Callable
from datetime import date, datetime
from .tests import test_args_list


def format_args(args: list, foo: Callable) -> NamedTuple:
	fullname = ' '.join(args[:3])
	birthdate = args[3]
	sex = args[4]

	test_args_list(foo, [fullname, birthdate, sex])

	class FormattedArgs(NamedTuple):
		if foo.__name__ == "post":
			fullname: str
			birthdate: date
			sex: str

		else:
			raise AttributeError(f"Function named '{foo.__name__}' wasn't found")

	birthdate = datetime.strptime(birthdate, "%d.%m.%Y").date()

	return FormattedArgs(fullname, birthdate, sex)

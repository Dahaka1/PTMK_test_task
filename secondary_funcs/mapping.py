from classes.person import Person
from secondary_funcs.other import generate_person_params, generate_person_started_with_F


def persons_params_list(args: list[tuple]) -> map:
	return map(lambda person_params: Person(*person_params), args)


def random_persons_list(count: int = 1000000) -> map:
	random_persons_params = (generate_person_params() for _ in range(count))
	return map(lambda params: Person(*params), random_persons_params)


def random_persons_startswith_f(count: int = 100) -> map:
	random_persons_startswith_f_params = (generate_person_started_with_F() for _ in range(count))
	return map(lambda params: Person(*params), random_persons_startswith_f_params)

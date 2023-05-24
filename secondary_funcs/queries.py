from database import conn
from typing import Callable, Iterable
from secondary_funcs import sql


def execute_all(foo: Callable, args: Iterable):
	if foo.__name__ == 'post_advanced':
		query = sql("post")
		with conn.cursor() as cursor:
			for person in args:
				params = person.fullname, person.birthdate, person.sex
				cursor.execute(query, params)



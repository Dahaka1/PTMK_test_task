from database import conn
from secondary_funcs import sql
from secondary_funcs.decorators import handle_func
from secondary_funcs.other import format_args
from secondary_funcs.mapping import persons_params_list
from secondary_funcs.represent import write_to_console_unique_persons, get_args
from secondary_funcs.queries import execute_all
from secondary_funcs.mapping import random_persons_list, random_persons_startswith_f
from loguru_logging import closing_info
from psycopg2.errors import DuplicateTable, UndefinedObject, DuplicateObject
from .strings import delete_indexes


@handle_func
def start() -> None:
	"""
	func number 1
	"""
	try:
		with conn.cursor() as cursor:
			cursor.execute(
				sql(start)
			)
	except DuplicateObject:
		raise Exception("Table or built-in type 'sex_choices' already exists. Remove them before making table")


@handle_func
def post(args=None):
	"""
	func number 2
	"""
	if not args is None and len(args) == 5:
		kwargs = format_args(args, post)
		with conn.cursor() as cursor:
			cursor.execute(
				sql(post),
				(kwargs.fullname,
				 kwargs.birthdate,
				 kwargs.sex)
			)
	else:
		raise AttributeError("Function needs for 5 arguments.")


@handle_func
def get():
	"""
	func number 3
	"""
	closing_info()
	with conn.cursor() as cursor:
		cursor.execute(sql(get))  # не смог до конца разобраться, как сделать оптимальный запрос SQL,
		# поэтому долго и медленно работает посредством использования ORM Person
		args = cursor.fetchall()
		persons = persons_params_list(args)
		write_to_console_unique_persons(persons)


@handle_func
def post_advanced():
	"""
	func number 4
	"""
	random_persons = random_persons_list()
	random_persons_starts_with_f = random_persons_startswith_f()
	closing_info()
	execute_all(post_advanced, random_persons)
	execute_all(post_advanced, random_persons_starts_with_f)


@handle_func
def get_advanced():
	"""
	func number 5
	"""
	with conn.cursor() as cursor:
		cursor.execute(
			sql(get_advanced)
		)
		get_args(
			cursor.fetchall()
		)


def update_db():
	"""
	func number 6
	"""
	get_advanced()
	with conn.cursor() as cursor:
		try:
			cursor.execute(delete_indexes)
		except UndefinedObject:
			pass
		try:
			cursor.execute(
				sql(update_db)
			)
		except DuplicateTable:
			raise Exception(
				"Tried to create DB indexes, but they're already exists"
			)
	get_advanced(current_func=update_db)


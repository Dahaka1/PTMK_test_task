from database import conn
from secondary_funcs import sql
from secondary_funcs.decorators import handle_func
from secondary_funcs.other import format_args


@handle_func
def start() -> None:
	"""
	func number 1
	"""
	with conn.cursor() as cursor:
		cursor.execute(
			sql(start)
		)


@handle_func
def post(args):
	"""
	func number 2
	"""
	if len(args) == 5:
		kwargs = format_args(args, post)
		with conn.cursor() as cursor:
			cursor.execute(
				sql(post),
				(kwargs.fullname,
				 kwargs.birthdate,
				 kwargs.sex)
			)
	else:
		raise AttributeError("Arguments amount must be 5.")


def get():
	"""
	func number 3
	"""
	pass


def post_additional():
	"""
	func number 4
	"""
	pass


def get_additional():
	"""
	func number 5
	"""
	pass


def update_db():
	"""
	func number 6
	"""
	pass

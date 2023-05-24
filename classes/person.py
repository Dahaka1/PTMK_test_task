from datetime import date
from secondary_funcs.other import formatted_date
from typing import Optional
from main_funcs.strings import get_all_persons


class Person:
	"""
	ORM of person
	"""
	def __init__(
		self,
		fullname: str,
		birthdate: date,
		sex: str = None
	):
		self.pk = None
		self.fullname = fullname
		self.birthdate = birthdate
		self.sex: Optional[str] = sex
		self.age: Optional[int] = None

	def __repr__(self):
		self.get_params()
		return self.fullname, formatted_date(self.birthdate), self.sex, self.age

	def __str__(self):
		return ', '.join(map(str, self.__repr__()))

	def get_age(self) -> None:
		today = date.today()
		age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
		self.age = age

	def get_pk_and_sex(self) -> None:
		for person in self.get_all_persons():
			# person looks like (1, 'Тестовый Андрей Иваныч', datetime.date(1995, 6, 25), 'male')
			if person[1] == self.fullname and person[2] == self.birthdate:
				if self.sex is None:
					self.sex = person[3]
				self.pk = person[0]
				break

	def get_params(self) -> None:
		self.get_pk_and_sex()
		self.get_age()

	@staticmethod
	def get_all_persons() -> list[tuple]:
		from database import conn
		with conn.cursor() as cursor:
			cursor.execute(get_all_persons)
			return cursor.fetchall()





from __future__ import annotations

from typing import NamedTuple
from . import settings
import json


def database_params():
	try:
		params = json.load(open('non_public/db_settings.json', encoding='utf-8'))
		if not all(params.values()):
			raise AttributeError
	except (FileNotFoundError, AttributeError):
		params = None

	class DatabaseConfig(NamedTuple):
		DB_NAME: str = settings.DATABASE["db_name"] if params is None else params["db_name"]
		USER: str = settings.DATABASE["user"] if params is None else params["user"]
		PASSWORD: str = settings.DATABASE["password"] if params is None else params["password"]
		HOST: str = settings.DATABASE["host"] if params is None else params["host"]
		PORT: str = settings.DATABASE["port"] if params is None else params["port"]
	return DatabaseConfig()


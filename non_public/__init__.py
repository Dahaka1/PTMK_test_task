from __future__ import annotations
from typing import NamedTuple
from . import settings


def database_params():
	class DatabaseConfig(NamedTuple):
		DB_NAME: str = settings.DATABASE["db_name"]
		USER: str = settings.DATABASE["user"]
		PASSWORD: str = settings.DATABASE["password"]
		HOST: str = settings.DATABASE["host"]
		PORT: str = settings.DATABASE["port"]

	return DatabaseConfig()


from loguru import logger
from typing import Optional


def get_sex_choices(lang_code: str) -> Optional[list[str]]:
	if lang_code == 'ru':
		return ['мужчина', 'женщина']
	elif lang_code == 'en':
		return ['male', 'female']
	else:
		logger.error(
			"Chosen language code in settings.py must be in ('en', 'ru')"
		)



from main_funcs.settings import language_code
from loguru import logger


birthdate_regex = r'[0-2]?\d\.[0-2]?\d.[0-4]?\d'

if language_code == 'ru':
	fullname_regex = r'^[А-ЯЁ][а-яё]*([-][А-ЯЁ][а-яё]*)?\s[А-ЯЁ][а-яё]*\s[А-ЯЁ][а-яё]*$'
elif language_code == 'en':
	fullname_regex = r'^[A-Z][a-z]*([-][A-z][a-z]*)?\s[A-Z][a-z]*\s[A-Z][a-z]*$'
else:
	logger.error(
		"Chosen language code in settings.py must be in ('en', 'ru')"
	)

from psycopg2 import connect
import non_public
from loguru import logger

db_params = non_public.database_params()


try:
	conn = connect(
			dbname=db_params.DB_NAME,
			user=db_params.USER,
			password=db_params.PASSWORD,
			host=db_params.HOST,
			port=db_params.PORT
		)
	conn.autocommit = True
except:
	conn = connect()
	logger.error(
		"Can't establish a connection to DB."
	)

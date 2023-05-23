from psycopg2 import connect
import business_logics
from loguru import logger

db_params = business_logics.database_params()


try:
	conn = connect(
			dbname=db_params.DB_NAME,
			user=db_params.USER,
			password=db_params.PASSWORD,
			host=db_params.HOST,
			port=db_params.PORT
		)
except:
	conn = None
	logger.error(
		"Can't establish a connection to DB."
	)

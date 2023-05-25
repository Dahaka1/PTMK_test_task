from .settings import sex_choices

formatted_choices = ', '.join(f"\'{sex}\'" for sex in sex_choices)

sql = {
	"start":
		f"CREATE TYPE sex_choices AS ENUM ({formatted_choices});" + \
		"""
			CREATE TABLE persons (
			person_id serial PRIMARY KEY,
			fullname VARCHAR(100) NOT NULL,
			birthdate DATE NOT NULL, 
			sex sex_choices NOT NULL
			);
			""",
	"post": """
			INSERT INTO persons (fullname, birthdate, sex) 
			VALUES (%s, %s, %s);
			""",
	"get": """
			SELECT DISTINCT fullname, birthdate FROM persons ORDER BY fullname;
			""",  # Я не смог понять, как сделать формулу для вывода нужного
	# списка сразу с ИД, поэтому пришлось фильтровать их
	# посредством языка... получился очень медленный вывод

	"get_advanced": "SELECT p.fullname, p.birthdate, p.sex FROM "
					f"persons AS p WHERE p.sex = '{sex_choices[0]}' AND "
					f"p.fullname LIKE 'F%' ORDER BY fullname;",
	"update_db":  """				  
				  CREATE INDEX person_sex_index ON persons (sex);
				  CREATE INDEX person_fullname_index ON persons (fullname) 
				  WHERE fullname LIKE 'F%';
				  """  ###
}

get_all_persons = """
	SELECT * FROM persons ORDER BY fullname;
"""

get_db_table_length = """
	SELECT COUNT(*) FROM persons;
"""

get_person = """
	SELECT person_id, sex FROM persons WHERE fullname = %s AND birthdate = %s ORDER BY fullname LIMIT 1;
"""

delete_indexes = """
	DROP INDEX person_fullname_index;
	DROP INDEX person_sex_index;
"""
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
			"""
}

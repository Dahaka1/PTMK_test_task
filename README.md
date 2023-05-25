# PTMK_test_task

# BUILTIN
Logging: Loguru.
VCS: Git.
Virtual Environment: Virtualenv (Python).
DB: PostgreSQL.
DB-connecting module: psycopg2.
Testing: simple built-in Python asserts.

REFLECTED IN requirements.txt

# USAGE
You can use this script using installed Python on your computer by doing Git-clone command or downloading "dist" folder
for use it without built-in Python.

Start main.py using command line being in the project directory by command:
- "python main.py *function_number* *args*".

DB connecting settings you can write optionally in:
- "non_public/db_settings.json" (if you are working with .exe dist of script);
- "non_public/settings.py" (if you are working with raw code of script).

# INTERPRETATION
After doing script the folders named "tests" and "loguru_logging" will be created in base project folder:
- In "loguru_logging" you could see detailed log of working program functions;
- In "tests" you could see results of working functions number 5 and 6 (handled DB lines amount and fixed time of working).
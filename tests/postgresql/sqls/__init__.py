import os
from pathlib import Path

from psycopg2 import connect
from sql_importer import init

db_url = os.environ.get("DB_URL", "postgres://postgres:postgres@localhost:5432/postgres")
connection = connect(db_url)

init(Path(__file__).parent, globals(), connection)

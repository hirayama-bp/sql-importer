import re
from enum import Enum
from pathlib import Path

__all__ = ["SQLType", "SQLLoader"]


class SQLType(Enum):
    POSTGRESQL = "postgresql"


class SQLLoader:
    def __init__(self, sql_type: SQLType):
        self.sql_type = sql_type

    @staticmethod
    def replace_postgresql_placeholder(sql_text: str) -> str:
        sql_text = re.sub(r":'(\w+)'", r"%(\1)s", sql_text)
        sql_text = re.sub(r"(?<!:):([A-Za-z][0-9A-Za-z_]+)", r"%(\1)s", sql_text)
        return sql_text

    def replace_placeholder(self, sql_text: str) -> str:
        if self.sql_type is SQLType.POSTGRESQL:
            return self.replace_postgresql_placeholder(sql_text)
        else:
            raise NotImplementedError

    def load_sql(self, sql_path: Path) -> str:
        with open(sql_path) as f:
            sql_text = f.read()
        return self.replace_placeholder(sql_text)

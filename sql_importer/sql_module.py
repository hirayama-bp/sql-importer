import os
import re
from pathlib import Path
from typing import Any, Dict, Iterator, List, Pattern, Union

from psycopg2.extensions import connection
from psycopg2.extras import DictCursor

__all__ = ["SQLModule"]

PLACEHOLDER_PATTERN: Pattern = re.compile(r"%\((\w+)\)s")


class SQLModule:
    def __init__(self, conn: connection, sql: str):
        self.conn = conn
        self.sql = sql

    def get_placeholders(self) -> List[str]:
        return [
            m.group(1)
            for m in PLACEHOLDER_PATTERN.finditer(self.sql)
        ]

    def check_enough_kwargs(self, kwargs: Dict[str, Any]):
        placeholders = self.get_placeholders() 
        for ph in placeholders:
            if ph not in kwargs:
                raise ValueError(f"placeholder '{ph}' is not passed.")

    def query(self, **kwargs: Any) -> Iterator[Dict[str, Any]]:
        self.check_enough_kwargs(kwargs)
        with self.conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(self.sql, kwargs)
            for row in cur:
                yield dict(row)

    def execute(self, **kwargs: Any) -> int:
        self.check_enough_kwargs(kwargs)
        with self.conn.cursor() as cur:
            cur.execute(self.sql, kwargs)
            row_count = cur.rowcount
        return row_count

import os
from pathlib import Path
from typing import Any, Dict, Union

from psycopg2.extensions import connection

from .sql_loader import SQLType, SQLLoader
from .sql_module import SQLModule

__all__ = ["init", "SQLType"]



def init(
        base_dir: Union[str, os.PathLike], 
        exports: Dict[str, Any], 
        connection: connection, 
        sql_type: SQLType = SQLType.POSTGRESQL, 
        import_ext: str = ".sql"
):
    base_path = Path(base_dir)
    import_grob = f"*.{import_ext}".replace("..", ".")
    loader = SQLLoader(sql_type)
    for sql_path in base_path.glob(import_grob):
        name = sql_path.stem
        sql = loader.load_sql(sql_path)
        exports[name] = SQLModule(connection, sql)

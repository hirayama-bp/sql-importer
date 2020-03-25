# sql-importer

![](https://github.com/beproud/sql-importer/workflows/ci/badge.svg)

Utility to import sql files as a python module.


## Requirements
- Python ^3.6

## Install

```
$ pip install sql-importer
```

## Usage

- You have to make `__init__.py` at the same directory which sql files have been placed on.
- And write like the following to the `__init__.py`:

```python
import os
from sql_importer import init
from psycopg2 import connect

connection = connect("postgres://postgres:postgres@localhost:5432/postgres")
## if using django:
# from django.db import connection

init(os.path.dirname(__file__), globals(), connection, sql_type='postgresql')
```

- That's all, you can import sql files (removed `.sql` suffix) as python modules.

  - Example: `testing/sql/sum_sales.sql` exists.

  ```sql
    SELECT SUM(price) AS sum_sales FROM sales
    WHERE
      sales_from >= :'sales_from'
      AND sales_to < :'sales_to'
    ;
  ```

  ```python
    from datetime import date
    from testing import sql
    sql.sum_sales.query(sales_from=date(2017, 5, 22), sales_to=date(2017, 12, 26))
  ```

  - `sql` object has 2 methods, both method execute the sql and receive variables as keyword arguments.

    :query: It returns records. it expects only what has one or more results like `select` query.
    :execute: It returns number of records affected by the SQL.

- Now `sql_type` argument allows `postgresql`.

  - If you want to use the other sql_type, please make the issue on https://github.com/beproud/sql-importer .

## Demo

### start up

```
$ git clone git@github.com:beproud/sql-importer.git
$ cd sql-importer
$ docker-compose up -d
$ docker-compose exec app ash
```

### Try

```
~/app # ls tests/postgresql/sqls
__init__.py  clear_table.sql  create_table.sql  delete_sale.sql  drop_table.sql  insert_sale.sql  select_sales.sql  update_sale.sql
~/app # poetry run python
```

```python
>>> from tests.postgresql import sql
>>> sql.create_table.execute()
-1
>>> sql.insert_sale.execute(name='apple', price=100)
1
>>> list(sql.select_sales.query())
[{'name': 'apple', 'price': 100}]
>>> sql.delete_sale.execute(name='orange')
0
>>> sql.delete_sale.execute(name='apple')
1
>>> list(sql.select_sales.query())
[]
```

### Unittest

```
~/app # make lint
~/app # make test
```


- This library is tested by only latest `postgresql`.

## Contributors
- aodag ( https://github.com/aodag )
- crohaco ( https://github.com/righ )
- hirayama ( https://github.com/hirayama-bp )

## Links
- https://github.com/beproud/sql-importer
- https://pypi.python.org/pypi/sql-importer

import pytest


@pytest.fixture(autouse=True, scope='module')
def init():
    from . import sqls
    sql.drop_table.execute()
    sql.create_table.execute()


@pytest.fixture(autouse=True, scope='function')
def clear():
    from . import sqls
    sql.clear_table.execute()

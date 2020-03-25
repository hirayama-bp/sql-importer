import pytest


@pytest.fixture(autouse=True, scope="module")
def init():
    from . import sqls

    sqls.drop_table.execute()
    sqls.create_table.execute()


@pytest.fixture(autouse=True, scope="function")
def clear():
    from . import sqls

    sqls.clear_table.execute()

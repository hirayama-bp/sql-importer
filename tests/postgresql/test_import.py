import pytest


@pytest.fixture
def sql():
    from . import sqls as _sql
    return _sql


def test_insert(sql):
    sql.insert_sale.execute(name='apple', price=100)
    sql.insert_sale.execute(name='orange', price=50)
    expected = [{'name': 'apple', 'price': 100}, {'name': 'orange', 'price': 50}]
    actual = list(sql.select.query())
    assert expected == actual


def test_delete(sql):
    sql.insert_sale.execute(name='apple', price=100)
    sql.insert_sale.execute(name='orange', price=50)
    sql.delete_sale.execute(name='apple')
    expected = [{'name': 'orange', 'price': 50}]
    actual = list(sql.select.query())
    assert expected == actual


def test_update(sql):
    sql.insert_sale.execute(name='apple', price=100)
    sql.update_sale.execute(name='apple', price=300)
    expected = [{'name': 'apple', 'price': 300}]
    actual = list(sql.select.query())
    assert expected == actual

import pytest


# @pytest.mark.parametrize 的使用：如何为一个测试函数提供多组输入输出数据。
@pytest.mark.parametrize('input,expected', [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 54),
])
def test_eval(input, expected):
    assert eval(input) == expected


@pytest.mark.parametrize('input', [1, 2, 5])
@pytest.mark.parametrize('expected', [2, 3, 6])
def test_eval2(input, expected):
    # 会执行2+1,2+2,2+5,3+1,3+2,3+5,6+1,6+2,6+5
    assert input + expected > 0


# 作用域

import pytest

"""
function（默认）：在每个测试函数前调用一次。
class：在每个测试类的所有测试函数前调用一次。
module：在模块级别调用一次，适用于模块内的所有测试函数。
session：在整个测试会话期间调用一次，适用于所有模块和测试。
"""


@pytest.fixture(scope="module")
def db_connection():
    print("Setting up DB connection")
    conn = "db_conn"
    yield conn
    print("Tearing down DB connection")


def test_query1(db_connection):
    assert db_connection == "db_conn"


def test_query2(db_connection):
    assert db_connection == "db_conn"


#Autouse Fixtures

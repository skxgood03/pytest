import pytest


# @pytest.mark.parametrize ��ʹ�ã����Ϊһ�����Ժ����ṩ��������������ݡ�
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
    # ��ִ��2+1,2+2,2+5,3+1,3+2,3+5,6+1,6+2,6+5
    assert input + expected > 0


# ������

import pytest

"""
function��Ĭ�ϣ�����ÿ�����Ժ���ǰ����һ�Ρ�
class����ÿ������������в��Ժ���ǰ����һ�Ρ�
module����ģ�鼶�����һ�Σ�������ģ���ڵ����в��Ժ�����
session�����������ԻỰ�ڼ����һ�Σ�����������ģ��Ͳ��ԡ�
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

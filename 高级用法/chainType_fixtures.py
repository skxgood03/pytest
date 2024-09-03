import pytest


# fixtures ���Ա˴�������һ�� fixture ����ʹ������ fixtures���γ���ʽ���á����ַ�ʽ���԰����㹹�����ӵĲ��Ի�����


@pytest.fixture
def db():
    print("Connecting to DB")
    return "db_connection"


@pytest.fixture
def user(db):
    print("Creating user with", db)
    return {"name": "Alice", "db": db}


def test_user(user):
    assert user["name"] == "Alice"
    assert user["db"] == "db_connection"
# user fixture ������ db fixture���� user ������ʱ��
# pytest �����ȵ��� db fixture�������������ݸ� user��
# ������ʽ���������㽫���Ի����ĸ������ַֿ��������ִ����ģ�黯��

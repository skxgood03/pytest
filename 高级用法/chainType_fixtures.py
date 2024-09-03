import pytest


# fixtures 可以彼此依赖，一个 fixture 可以使用其他 fixtures，形成链式调用。这种方式可以帮助你构建复杂的测试环境。


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
# user fixture 依赖于 db fixture。当 user 被调用时，
# pytest 会首先调用 db fixture，并将其结果传递给 user。
# 这种链式调用允许你将测试环境的各个部分分开处理，保持代码的模块化。

import pytest


# 在某些情况下，fixture 需要根据测试的上下文动态生成，比如根据传入的参数来生成不同的测试数据。request 对象在 fixture 中可以帮助实现这一点。

@pytest.fixture
def user(request):
    name = request.param
    return {"name": name}


@pytest.mark.parametrize("user", ["Alice", "Bob"], indirect=True)
def test_user(user):
    assert user["name"] in ["Alice", "Bob"]
# 在这个示例中，user fixture 根据传递的参数动态生成。indirect=True 参数告诉
# pytest 通过 fixture 的方式来处理参数。
# 测试函数 test_user 会分别用 "Alice" 和 "Bob" 两种不同的数据运行。

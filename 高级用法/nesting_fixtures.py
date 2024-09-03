import pytest


# fixtures 也可以通过嵌套的方式来复用功能，例如在不同的作用域下使用相同的基础设置。
@pytest.fixture(scope="session")
def session_setup():
    print("Session-wide setup")
    return "session_data"


@pytest.fixture(scope="module")
def module_setup(session_setup):
    print(f"Module setup using {session_setup}")
    return "module_data"


@pytest.fixture(scope="function")
def function_setup(module_setup):
    print(f"Function setup using {module_setup}")
    return "function_data"


def test_example1(function_setup):
    assert function_setup == "function_data"


def test_example2(function_setup):
    assert function_setup == "function_data"

# 这里 function_setup 依赖于 module_setup，而 module_setup 又依赖于 session_setup。
# 测试函数 test_example1 和 test_example2 都使用了 function_setup，
# 而在不同的作用域下，fixtures 的结果是逐层传递的，构建起一个完整的测试环境。

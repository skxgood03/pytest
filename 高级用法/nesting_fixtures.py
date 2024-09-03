import pytest


# fixtures Ҳ����ͨ��Ƕ�׵ķ�ʽ�����ù��ܣ������ڲ�ͬ����������ʹ����ͬ�Ļ������á�
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

# ���� function_setup ������ module_setup���� module_setup �������� session_setup��
# ���Ժ��� test_example1 �� test_example2 ��ʹ���� function_setup��
# ���ڲ�ͬ���������£�fixtures �Ľ������㴫�ݵģ�������һ�������Ĳ��Ի�����

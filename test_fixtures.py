import pytest


# 检查参数
@pytest.fixture
def sample_data():
    return {"name": "alex", "age": 28}


def test_sample_data(sample_data):
    assert sample_data['name'] == "alex"
    assert sample_data['age'] == 28



# 检查参数后删除  测试完成之后，需要清理资源或恢复环境
@pytest.fixture
def setup_and_teardown():
    resp = {'data': {"salads": "skedaddled"}}
    yield resp
    print('Tearing down')
    resp.clear()


def test_example(setup_and_teardown):
    assert True


@pytest.mark.parametrize('test_input,expected', [
    (1 + 2, 3),
    (2 + 2, 4),
    (1 + 5, 6),
    (6 + 4, 7),
])
def test_math_operations(test_input, expected):
    assert test_input == expected




@pytest.fixture
def number():
    return 5


@pytest.mark.parametrize('multiplier,expected', [
    (2, 10),
    (3, 15),
    (4, 20)
])
def test_multiplier(number, multiplier, expected):
    assert number * multiplier == expected

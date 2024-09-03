# 模块名必须以 test_ 开头 或  _test结尾 如：demo_test.py  test_demo2.py
# 函数必须以 test_ 开头
# 类必须以Test开头 并且不能有 __init__方法


def fun(x):
    return x + 1


def test_answer():
    assert fun(3) == 6


def test_str():
    assert str(1) == "1"


def test_list():
    assert [1,2,3] == [1, 2]

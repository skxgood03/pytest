# ģ���������� test_ ��ͷ ��  _test��β �磺demo_test.py  test_demo2.py
# ���������� test_ ��ͷ
# �������Test��ͷ ���Ҳ����� __init__����


def fun(x):
    return x + 1


def test_answer():
    assert fun(3) == 6


def test_str():
    assert str(1) == "1"


def test_list():
    assert [1,2,3] == [1, 2]

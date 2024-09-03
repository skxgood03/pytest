import pytest


# ��ĳЩ����£�fixture ��Ҫ���ݲ��Ե������Ķ�̬���ɣ�������ݴ���Ĳ��������ɲ�ͬ�Ĳ������ݡ�request ������ fixture �п��԰���ʵ����һ�㡣

@pytest.fixture
def user(request):
    name = request.param
    return {"name": name}


@pytest.mark.parametrize("user", ["Alice", "Bob"], indirect=True)
def test_user(user):
    assert user["name"] in ["Alice", "Bob"]
# �����ʾ���У�user fixture ���ݴ��ݵĲ�����̬���ɡ�indirect=True ��������
# pytest ͨ�� fixture �ķ�ʽ�����������
# ���Ժ��� test_user ��ֱ��� "Alice" �� "Bob" ���ֲ�ͬ���������С�

import pytest

data = [1, 2, 3]


@pytest.fixture(params=data)
def myfixture(request):
    return request.param, request.config


def test_one(myfixture):
    print(myfixture)
if __name__ == '__main__':
    test_one()
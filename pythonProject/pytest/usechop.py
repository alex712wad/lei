# import pytest
# @pytest.fixture()
# def chopstick():
#     print("before")
#     yield 100
#     print('after')
# @pytest.fixture(params=[1,2,3])
# def init_data(request):
#     print('参数',request.param)
#     return request.param
#
# def test_data(init_data):
#    assert init_data<20
# @pytest.mark.parametrize(['a','b'],[(1,2),(3,4),(5,6)])
# def test_add(a,b):
#     print('sum：%d'%(a+b))
# @pytest.mark.usefixtures('chopstick')
# def test_01(chopstick):
#     assert chopstick == 100
#     print(111)
# @pytest.mark.parametrize(['a','b'],[(2,1),(2,8)])
# def test_jian(login,a,b):
#     print('num：%d'%(a-b))


import pytest
@pytest.fixture(scope='function')
def myfixture_function():
    print("开始加载function级别夹具")
    yield 100
    print("开始退出function级别夹具")
@pytest.fixture(scope='class')
def myfixture_class():
    print("开始加载class级别夹具")
    yield 200
    print("开始退出class级别夹具")
@pytest.fixture(scope='module')
def myfixture_module():
    print("开始加载module级别夹具")
    yield 300
    print("开始退出module级别夹具")
@pytest.fixture(scope='session', autouse=True)
def myfixture_session():
    print("开始加载session级别夹具")
    yield 400
    print("开始退出session级别夹具")
def test_session(myfixture_function):
    assert myfixture_function == 100


pytestmark = pytest.mark.usefixtures('myfixture_module')


@pytest.mark.usefixtures('myfixture_class')
class TestFixture:

    def test_two(self, myfixture_function):
        assert myfixture_function == 100

    def test_three(self):
        pass

if __name__ == '__main__':
    pytest.main(['-s','./usechop.py'])
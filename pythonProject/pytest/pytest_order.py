import pytest
#有标记的先于未标记的然后标记order若不小于0则order越小优先级越高 0 1 2 3 4 如果order为附属则越大优先级越高 -1  -2  -3  -4
# 0 1 2 3 4 未标记的  -1 -2 -3
@pytest.mark.run(order=-1)
def test_1():
    print('1')
@pytest.mark.run(order=-1)
def test_2():
    print('2')
@pytest.mark.run(order=-0)
def test_3():
    print('3')
@pytest.mark.run(order=1)
def test_4():
    print('4')
@pytest.mark.run(order=2)
def test_5():
    print('5')
@pytest.mark.run(order=3)
def test_6():
    print('6')
if __name__ == '__main__':
    pytest.main('-s','./pytest_order.py')
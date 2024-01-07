import pytest
@pytest.mark.parametrize(['a','b'],[(1,2),(2,2),(3,2),(4,2),(50,61)])
def demo_a(a,b):
    print("demo_a+++++++++++++")
    assert a+b>100,"结果小于等于100"


if __name__ == '__main__':
    pytest.main(['-s','test6.py'])

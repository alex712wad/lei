import pytest
def test_3():
    print("test_333333+++++")
    return 1 * 0
def test_4():
    print('test_444444+++++')
    return 1 + 1
#跳过
@pytest.mark.skip(reason='除数为0')
def demo_5():
    print("demo_5+++++")
    return 1 / 0
#允许失败
@pytest.mark.xfail(raises=Exception)
def demo_6():
    print("demo_6666666+++++")
    return 1 / 0


if __name__ == '__main__':
    pytest.main(['-s','test5.py'])

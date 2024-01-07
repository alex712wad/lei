import pytest
def test_a():
    print("test_a+++++")
    return 1 * 0
def test_b():
    try:
        c = 1 / 0
    except Exception as e:
        print(e)
if __name__=='__main__':
    # test_a()
    test_b()
    #默认测试时不显示所测函数内的打印如果要打印需配置参数
    pytest.main(['-s'])

#单元测试 1测试函数 类 方法能不能够正常运行 2.测试执行的结果是否符合我们的预期结果  断言
import pytest
def test_a():
    print("test_a+++++")
    assert 1==1
def test_b():
    print('test_b+++++')
    assert 'a' in 'hello'
if __name__=='__main__':
    # test_a()
    # test_b()
    #默认测试时不显示所测函数内的打印如果要打印需配置参数
    pytest.main(['-s','test4.py'])

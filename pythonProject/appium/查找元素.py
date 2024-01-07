from appium import webdriver
from appium.webdriver.common.appiumby import By
#链接设备所必须的参数如 系统（安卓 ios） 系统版本  要启动的app的名称（包名） 要启动的app的界面
dict={}
dict['platformName']='Android'
#获取手机Android的版本
#adb shell getprop ro.build.version.release
#获取当前运行的程序和界面的名字
#adb shell dumpsys window windows | findstr eFocusedApp
dict['platformVersion']='5.1'
dict['deviceName']='192.168.56.101:1234'
dict['appPackage']='com.android.settings'
dict['appActivity']='.settings'
#虚拟手机的ip
driver = webdriver.Remote('http://127.0.0.1:8080/wd/hub',desired_capabilities=dict)
#关闭应用
driver.close_app()
#关闭链接
driver.quit()
#元素定位
#                       //*表示选取所有元素  然后限定条件[]里面写具体限定条件
driver.find_element(By.XPATH,'//*[text()="显示"]').click()
#                               上面是拿文本下面是拿属性 <a>123</a>     <a text='123' />
driver.find_element(By.XPATH,'//*[@text="显示"]').click()
element = driver.find_element(By.id,'1')
#unicode设置允许中文输入(老的版本会需要设置)
# dict['unicodeKeyboard']='True'
#键盘设置允许输入
# dict['resetKeyboard']='True'
element.send_keys('1232terfwer')
#清楚输入的内容
element.clear()
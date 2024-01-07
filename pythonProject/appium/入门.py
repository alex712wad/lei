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
#安装指定路径的app(安装包的路径在电脑上的路径)
driver.install_app('app的路径')
#删除名字为XX的app
driver.remove_app('app名字')
#判断某个app是否安装
driver.is_app_installed('应用的包名')
#将内容放到目标位置去
driver.push_file('目标位置','内容')
#拉取指定目标位置的文件
print(driver.pull_file('目标位置'))
#获取界面的xml源码
print(driver.page_source)
#元素定位
driver.find_element(By.ID,'1')
#获取当前操作的应用的包名
print(driver.current_package)
#获取当前操作的界面名
print(driver.current_activity)
#获取id为1的元素
element = driver.find_element(By.id,'1')
#打印元素的内容
print(element.text)
#单机元素
element.click()
#获取元素属性为id的值
element.get_attribute('id')
#获取元素的位置（元素左上角相对于屏幕左上角）
print(element.location)
#获取元素的尺寸（返回一个字典）
print(element.size)
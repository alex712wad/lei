from appium import webdriver
from appium.webdriver.common.appiumby import By
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
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
#unicode设置允许中文输入(老的版本会需要设置)
# dict['unicodeKeyboard']='True'
#键盘设置允许输入
# dict['resetKeyboard']='True'
#虚拟手机的ip
driver = webdriver.Remote('http://127.0.0.1:8080/wd/hub',desired_capabilities=dict)
#关闭应用
driver.close_app()
#duration默认是600毫秒
driver.swipe(start_x=270,start_y=640,end_x=270,end_y=120,duration=600)
#从元素1滚动到元素2
driver.scroll(driver.find_element(By.ID,'1'),driver.find_element(By.ID,'2'))
#拖拽功能
driver.drag_and_drop(driver.find_element(By.ID,'1'),driver.find_element(By.ID,'2'))
#高级模拟手势
# 按下
#TouchAction(driver).press(self,el,x,y,duration)
# 长按(默认长按1000毫秒)
#TouchAction(driver).press(self,el,x,y,duration)
# 移动
# TouchAction(driver).move_to(self,el,x,y)
# 等待                      ms=时间
# TouchAction(driver).wait(self,ms)
# 松手
# TouchAction(driver).release()
#轻击 count=次数  tap和click的区别是click有延迟触发效果（为了检验是否是双击如果要双击要用tap）
# TouchAction(driver).tap(self,element,x,y,count)
# action=TouchAction(driver)
# el1=driver.find_element(By.XPATH,'//*[@text="bbb"]')
# el2=driver.find_element(By.XPATH,'//*[@text="aaa"]')
#滑动必须搭配wait
# action.press(el1).wait(3).move_to(el2).release()
# action.perform()
# 滑动案例(设置图案解锁Z)
# sleep(3)
# el1=driver.find_element(By.XPATH,'//*[@text=声音]')
# el2=driver.find_element(By.XPATH,'//*[@text=WLAN]')
# action = TouchAction(driver)
# action.press(el1).wait(500).move_to(el2).release()
# action.perform()#执行以上操作
# driver.find_element(By.XPATH,'//*[@text=安全]').click()
# sleep(1)
# driver.find_element(By.XPATH,'//*[@text=屏幕锁定]').click()
# sleep(1)
# driver.find_element(By.XPATH,'//*[@text=图案]').click()
# sleep(1)
# #设置图形
# action.press(x=105,y=450).wait(200).move_to(270,450).wait(200).move_to(435,450).wait(200).move_to(270,615).wait(200).move_to(105,780).wait(200).move_to(270,780).wait(200).move_to(435,780).release()
# action.perform()
#其他操作
# driver.device_time #获取时间
# driver.get_window_size()#获取手机屏幕大小
# driver.network_connection#获取手机网络信息
# driver.set_network_connection()#设置手机网络信息 1飞行模式 2wifi 4移动数据 6=wifi+移动数据
# driver.keyevent()#点击按键
# driver.get_screenshot_as_file('1.png')#截屏并保存只支持png格式
# driver.save_screenshot()
# driver.open_notifications()#打开通知栏
# #关闭链接
driver.quit()

# 字典
from appium import webdriver

desired_caps={
    "platformName":"Android",
    "platformVersion":"6.0.1",
    "deviceName":"yjy02",
    "appPackage":"com.km.karaoke",
    "appActivity":"com.utalk.hsing.activity.StartActivity",
    "noReset":True
}

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

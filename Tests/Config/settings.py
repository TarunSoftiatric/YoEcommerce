"""
Global configs
"""
from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "2cbede98",
    "app": "D:appdebug.apk",
    "appPackage": "com.fatbit.yokartv9.buyer",
    "appActivity": ".activity.SplashActivity"
}

remote_driver_url = 'http://127.0.0.1:4723/wd/hub'
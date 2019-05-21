#encoding=utf-8
from selenium import webdriver
import time
from Util.ObjectMap import *
from ProjectVar.Var import *
from Util.DirandFile import *
import traceback
from selenium.webdriver.chrome.options import Options

"""#定义全局的浏览器driver变量"""
driver1 = None
def open_browser(browserName,*arg):
    global driver1
    try:
        if browserName.lower().strip()=="ie":
            driver1 = webdriver.Ie(executable_path=ieDriverFilePath)
        elif browserName.lower().strip()=="chrome":
            driver1 = webdriver.Chrome(executable_path=chromeDriverFilePath)
        else:
            driver1 = webdriver.Firefox(executable_path=firefoxDriverFilePath)

    except Exception,e:
        raise e

def visit_url(url,*arg):
    global driver1
    try:
        driver1.get(url)
    except Exception,e:
        raise e
def pause(seconds,*arg):
    time.sleep(float(seconds))

def close_browser(*arg):
    global driver1
    try:
        driver1.quit()
    except Exception,e:
        raise e

def enter_frame(locatorMethod,locatorExpression,*arg):
    global driver1
    try:
        driver1.switch_to.frame(getElement(driver1,locatorMethod,locatorExpression))
    except Exception,e:
        raise e
        print "can not enter frame!"

def input_string(locatorMethod,locatorExpression,content,*arg):
    try:
        getElement(driver1,locatorMethod,locatorExpression).clear()
        getElement(driver1,locatorMethod,locatorExpression).send_keys(content)
    except Exception,e:
        raise e

def click(locatorMethod,locatorExpression,*arg):
    try:
        getElement(driver1,locatorMethod,locatorExpression).click()
    except Exception,e:
        raise e

def login(usernameAndpassword,*arg):
    username,password=usernameAndpassword.split("||")
    open_browser("ie")
    visit_url("http://mail.163.com")
    pause(3)
    enter_frame('xpath',"//div[@id='loginDiv']//iframe")
    pause(2)
    input_string("xpath","//input[@name='name']",username)
    input_string("xpath","//input[@name='password']",password)
    pause(3)
    click("id","dologin")
    pause(3)
    assert_word(u"退出")

def assert_word(expected_word,*arg):
    try:
        assert True == (expected_word in driver1.page_source)
    except AssertionError,e:
        raise e
    except Exception,e:
        raise e

def capture_error_screen():
    global driver1
    createDir(project_path+"\\ScreenPictures\\ErrorPicture",time.strftime("%Y-%m-%d",time.localtime()))
    filename = "%s\\ScreenPictures\\ErrorPicture\\%s\\%s.png"%(project_path,time.strftime("%Y-%m-%d",time.localtime()),time.strftime("%H:%M:%S",time.localtime()))
    try:
        driver1.get_screenshot_as_file(filename)
        print type(driver1)
    except Exception,e:
        raise e
    return filename



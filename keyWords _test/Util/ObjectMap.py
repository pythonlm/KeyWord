#encoding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
#获取单个页面元素对象
def getElement(driver,locateType,locatorExpression):
    try:
        element = WebDriverWait(driver,5).until\
            (lambda x:x.find_element(by = locateType,value = locatorExpression))
        return element
    except Exception,e:
        raise e

#获取多个相同页面元素对象，以list返回
def getElements(driver,locateType,locatorExpression):
    try:
        elements = WebDriverWait(driver,5).until\
            (lambda x:x.find_element(by=locateType,value=locatorExpression))
        return enumerate
    except Exception,e:
        raise e

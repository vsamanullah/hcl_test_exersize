'''
This file provides utilities to related web driver via selenuim module for given browser
'''

''' System Imports '''
from selenium import webdriver
import enum

''' User defined imports'''
import Configuration.WebConfig
import CoreLibraries.ReadWindowsReg as Reg


# enum with all browser types
class BrowserTypeEnum(enum.Enum):
    chrome = 1
    firefox = 2
    ie = 3
    edge = 4


# dictionary with all the browser types
BrowserTypeDictMap = {"chrome": BrowserTypeEnum.chrome,
                      "firefox": BrowserTypeEnum.firefox,
                      "ie": BrowserTypeEnum.ie,
                      "edge": BrowserTypeEnum.edge
                      }


# To set the browser type
def SetBrowserType(BrowserType):
    if not BrowserType in BrowserTypeDictMap:
        assert False, "Invalid Browser type " + BrowserType
    # for chrome browser
    if BrowserTypeDictMap[BrowserType] == BrowserTypeEnum.chrome:
        driver_web = webdriver.Chrome(Configuration.WebConfig.chrome_driver)
    # for fire fox browser
    elif BrowserTypeDictMap[BrowserType] == BrowserTypeEnum.firefox:
        driver_web = webdriver.Firefox(executable_path=Configuration.WebConfig.firefox_driver)
    # for ie browser
    # here we need some special set up
    # we need to change windows registry and then zoom the browser
    elif BrowserTypeDictMap[BrowserType] == BrowserTypeEnum.ie:
        if Reg.getDisplayScale() != 100:
            print (Reg.getDisplayScale())
            assert False , "Display settings should be 100% for ie browser"
        print("before ie driver")
        driver_web = webdriver.Ie(executable_path=Configuration.WebConfig.ie_driver)
        print("after ie driver")
        driver_web.execute_script("document.body.style.zoom='zoom %'")
        print("after set zoom")
    # for edge browser
    elif BrowserTypeDictMap[BrowserType] == BrowserTypeEnum.edge:
        driver_web = webdriver.Edge(Configuration.WebConfig.edge_driver)
    return driver_web

# Initialise web driver and provide default time outs to locate the elements
def InitializeDriver(BrowserType):
    print("Intializing the existing web driver " )
    driver_web = SetBrowserType(BrowserType)
    driver_web.get(Configuration.WebConfig.project_web_url)
    driver_web.maximize_window()
    # Set default timeouts
    driver_web.set_page_load_timeout(30)
    driver_web.implicitly_wait(10)
    return driver_web


# quit the web driver after performing all actions
def CloseDriver(driver_web):
    print("Closing the existing web driver" + str(driver_web))
    # driver_web.close()
    driver_web.quit()

'''
Global variables to store
example browser name
this will help to access the parameter accross the modules
'''
SUT_browser = False
web_browser_name = "None"


def set_variable_browser(value):
    global SUT_browser
    SUT_browser = value


def get_variable_browser():
    return SUT_browser


def set_web_browser_name(browser_name):
    global web_browser_name
    web_browser_name = browser_name


def get_web_browser_name():
    return web_browser_name








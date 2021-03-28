'''
System import
'''
from selenium.webdriver.support.ui import WebDriverWait

'''
Generic find element method for finding element with and without wait, 
by taking the xpath and EC values from ObjRepo.ObjDict dictionary
'''


def generic_find_element(driver_web, dict, key, wait = 60):
    if len(dict[key]) > 2:
        ele = WebDriverWait(driver_web, wait).until(dict[key][2]((dict[key][0], dict[key][1])))
        return ele
    else:
        ele = driver_web.find_element(dict[key][0], dict[key][1])
        return ele

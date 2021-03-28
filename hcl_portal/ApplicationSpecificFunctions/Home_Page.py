'''
This file includes all the function to automate home page
'''

'''System imports'''

'''user defined imports'''
import CoreLibraries.LocatorLibrary as fe  # for locator module
import ObjectRepository.ObjRepo as Obj     # for the object repository


''' function to check if we reached home page by checking the HCL logo'''
def check_if_we_landed_in_home_page(driver_web):
    try:
        fe.generic_find_element(driver_web, Obj.ObjDict, Obj.HomePageLogo,10)
    except:
        assert False, "Home page is not loaded , hence aborting"

def accept_cookies_in_home_page(driver_web):
    try:
        fe.generic_find_element(driver_web, Obj.ObjDict, Obj.HomeCookiesBtn,10).click()
    except:
        assert False, "Not able to accept the cookies in home page , hence aborting"

def click_leadrership_link_in_home_page(driver_web):
    try:
        fe.generic_find_element(driver_web, Obj.ObjDict, Obj.LeaderShipLink,10).click()
    except:
        assert False, "Not click the Leadership link in home page , hence aborting"







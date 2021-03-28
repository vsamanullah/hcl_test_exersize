'''System imports'''
import time
from selenium import webdriver


'''user defined imports'''
import CoreLibraries.LocatorLibrary as fe  # for locator module
import ObjectRepository.ObjRepo as Obj     # for the object repository

'''
this function locates the list of directors by scrolling down to board of director table
returns all the members of the board of director
'''
def list_the_board_directors(driver_web):

    try:
        found_element = fe.generic_find_element(driver_web, Obj.ObjDict, Obj.DirectorsNaming,30)
        driver_web.execute_script("arguments[0].scrollIntoView();", found_element)
        # it is possible to find the child element for the parent "div.directors.naming" that is "ul" as below
        # find_child = found_element.find_elements_by_xpath("ul")
        # then iterate over li class to find Shiv
        # But I feel below is very simple and efficient , by getting the inner text
        list_items = found_element.get_attribute('innerText').split('\n')
        return list_items,found_element
    except:
        assert False, "Not able to find the Board of director in leadership page , hence aborting"

'''
this funtion takes list of directors table element as input 
then iterates over the child items to find the image url for the given board of director
'''
def retrive_image_url_of_the_board_directors(parent_element,board_director):
    try:
        found_childs = parent_element.find_elements_by_xpath("ul/li")
        found = 0
        for child in found_childs:
            if child.get_attribute('innerText').strip() == board_director:
                found = 1
                img_ele = child.find_elements_by_xpath("div/img")
                return img_ele[0].get_attribute('src').strip()
        if found == 0:
            assert False, "Not able to find the image url for Board of director %s , hence aborting" %(board_director)
    except:
        assert False, "Not able to find the image url for Board of director %s , hence aborting" % (board_director)



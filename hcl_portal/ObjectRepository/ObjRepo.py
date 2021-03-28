from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

''' This is place holder to locate the objects in the webpage'''

''' Home page locator'''
HomePageLogo = "HomePageLogo"
HomeCookiesBtn = "HomeCookiesBtn"
LeaderShipLink = "LeaderShipLink"

''' Leader ship page locator'''
DirectorsNaming = "DirectorsNaming"

# format of the dict is key is the locator name , values are  [type of locator , location identifier , availability/visibility]
ObjDict = {
            HomePageLogo: [By.XPATH, "//*[@id=\"Path_280\"]", ec.visibility_of_element_located],
            HomeCookiesBtn: [By.XPATH, "//*[@id=\"onetrust-accept-btn-handler\"]", ec.visibility_of_element_located],
            LeaderShipLink: [By.LINK_TEXT, "Leadership", ec.visibility_of_element_located],
            DirectorsNaming: [By.CSS_SELECTOR, "div.directors.naming", ec.visibility_of_element_located],
          }

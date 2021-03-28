'''
this file is the entry point to run the test
'''

'''system imports'''

import os
from pathlib import Path
import argparse
import unittest
import inspect


'''user imports for utilities'''
import Configuration.GenericConfig
import Configuration.WebConfig
import CoreLibraries.WebDriver
import CoreLibraries.FileManger as F_MNG
import CoreLibraries.UrlUtilities as URL_UT


'''user imports for Applicatiom specific'''
import ApplicationSpecificFunctions.Home_Page as HP
import ApplicationSpecificFunctions.LeaderShip_Page as LP
import TestData.TesDataSet as TST_SET

'''
parses the command line argument to run the test
creates the report diecroty for test report and 
under report directory it creates snap shot directory to download and store the screen shots
'''
def perform_intial_set_up():
    # Command line arguments
    parser = argparse.ArgumentParser(description='Runs the tests on a specified browser for Web applications')
    parser.add_argument("-b", "--browser", type=str, help="browser type : supported values are chrome, firefox, ie, edge",
                        choices=["chrome", "firefox", "ie", "edge"], default="chrome")

    args = parser.parse_args()
    print("args: " + str(args))

    # Setting the report path
    ProgramName = os.path.abspath(__file__)
    Program_execution_path = os.path.dirname(ProgramName)
    # Creating test report directory
    tstRepDir = str(Path(Program_execution_path) / Configuration.GenericConfig.test_report_dir)
    F_MNG.create_directory(tstRepDir)
    #creating the snapshot directory
    SnapShotDir = str(Path(tstRepDir) / Configuration.GenericConfig.screenshot_dir)
    F_MNG.create_directory(SnapShotDir)


    # For setting up the web driver paths
    SeleniumBrowserDriverPath = str(Path(Program_execution_path) / Configuration.WebConfig.selenium_browser_driver_path)
    os.environ["PATH"] += os.pathsep + SeleniumBrowserDriverPath

    #return the name of browser to be used for testing
    return args.browser,tstRepDir,SnapShotDir


class MySeleniumTests(unittest.TestCase):

    # setup : initialize the selenium webdriver for the given browser
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        browser, cls.tstRepDir, cls.SnapShotDir = perform_intial_set_up()
        cls.driver_web = CoreLibraries.WebDriver.InitializeDriver(browser)

    # teardown : close the session once the test is done
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        CoreLibraries.WebDriver.CloseDriver(cls.driver_web)

    # test check the shiv nadar is part of HCL board of directors
    def test_board_of_member(self):
        HP.check_if_we_landed_in_home_page(self.driver_web)
        HP.accept_cookies_in_home_page(self.driver_web)
        HP.click_leadrership_link_in_home_page(self.driver_web)
        list_of_board_members,found_element = LP.list_the_board_directors(self.driver_web)
        fn_name = inspect.currentframe().f_code.co_name
        print("Running the function %s to check if %s is part of %s" %(fn_name,TST_SET.board_of_directors_str,TST_SET.shiv_nadar_str))
        self.assertEqual(list_of_board_members[0].strip(),TST_SET.board_of_directors_str, "Director listing table should have Board of director item")
        self.assertEqual(list_of_board_members[1].strip(), TST_SET.shiv_nadar_str,"Board of director should have Shiv Nadar")
        print("test passed")

        # down load the image of board member
        image_src_path = LP.retrive_image_url_of_the_board_directors(found_element, TST_SET.shiv_nadar_str)
        image_file_name = URL_UT.get_file_name_from_url(image_src_path)
        image_save_path = str(Path(self.SnapShotDir) / image_file_name)
        print("downloading the file %s from the URL %s to local directory %s" %(image_file_name,image_src_path,image_save_path) )
        URL_UT.save_file_from_url(image_src_path,image_save_path )
        print("Image downloaded successfully and test passed")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MySeleniumTests("test_board_of_member"))
    runner = unittest.TextTestRunner()
    runner.run(suite)


    


    








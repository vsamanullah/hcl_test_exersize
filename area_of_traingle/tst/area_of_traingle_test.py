# system imports
import unittest
import sys
import os
import inspect
from contextlib import redirect_stdout

# adding user import paths
program_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(program_path, "../src"))

# user imports
import area_of_traingle as AT

# this is to limit the folating point comparison up to 0.0001
def float_equal(fl_num_a, fl_num_b):
    epsilon_val = 0.0001
    return abs(fl_num_a - fl_num_b) < epsilon_val

# Test class that implements the tests
class Test_Area_Of_Traingle(unittest.TestCase):
    def __init__(self, methodName='', side_a=None , side_b=None , side_c=None , expected_output = None ):
        super(Test_Area_Of_Traingle, self).__init__(methodName)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.expected_output = expected_output
        self.epsilon_val = 0.0001



    # to test : invalid test cases
    def test_area_of_traingle_function_invalid_case(self):
        fn_name = inspect.currentframe().f_code.co_name
        print("running the test %s with parameters sides %s %s %s"  %(fn_name,str(self.side_a),str(self.side_b),str(self.side_c)))
        self.assertEqual(AT.calculate_area_of_traingle(self.side_a,self.side_b,self.side_c), self.expected_output)

    # to test : valid test cases
    def test_area_of_traingle_function_valid_case(self):
        fn_name = inspect.currentframe().f_code.co_name
        print("running the test %s with parameters sides %s %s %s" % (fn_name, str(self.side_a), str(self.side_b), str(self.side_c)))
        self.assertEqual(float_equal(AT.calculate_area_of_traingle(self.side_a,self.side_b,self.side_c),self.expected_output),1)


if __name__ == '__main__':
    suite = unittest.TestSuite()

    #negative value side check
    suite.addTest(Test_Area_Of_Traingle("test_area_of_traingle_function_invalid_case" , -1 ,0 , 0 , -1))
    suite.addTest(Test_Area_Of_Traingle("test_area_of_traingle_function_invalid_case" , 0, -4 , 0, -1))
    suite.addTest(Test_Area_Of_Traingle("test_area_of_traingle_function_invalid_case", 0, 0, -0.1, -1))

    # zero side check
    suite.addTest(Test_Area_Of_Traingle("test_area_of_traingle_function_invalid_case" , 0 ,2 , 4 , -1))
    suite.addTest(Test_Area_Of_Traingle("test_area_of_traingle_function_invalid_case" , 1, 0 , 0.1, -1))
    suite.addTest(Test_Area_Of_Traingle("test_area_of_traingle_function_invalid_case", 2, 0.001, 0, -1))

    # invalid data type - characters
    suite.addTest(Test_Area_Of_Traingle("test_area_of_traingle_function_invalid_case" , "a" ,2 , 4 , -2))
    suite.addTest(Test_Area_Of_Traingle("test_area_of_traingle_function_invalid_case" , 1, 'b' , 0.1, -2))
    suite.addTest(Test_Area_Of_Traingle("test_area_of_traingle_function_invalid_case", 2, 0.001, "+", -2))

    # valid case
    suite.addTest(Test_Area_Of_Traingle("test_area_of_traingle_function_valid_case", 100, 50 , 5, 11587.43932))
    suite.addTest(Test_Area_Of_Traingle("test_area_of_traingle_function_valid_case", 100, 50, 25.5, 15793.54159))
    suite.addTest(Test_Area_Of_Traingle("test_area_of_traingle_function_valid_case", 100.5, 50.75, 25.5, 16026.27532))

    runner = unittest.TextTestRunner()
    runner.run(suite)

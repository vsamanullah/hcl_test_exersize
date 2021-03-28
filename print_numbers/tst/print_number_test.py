# system imports
import unittest
import sys
import os
import io
from contextlib import redirect_stdout

# adding user import paths
program_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(program_path, "../src"))

# user imports
import print_number as PN

# calls the passed funtion and capture its out put
def call_the_function(function_name_to_be_called):
    fie_io = io.StringIO()
    with redirect_stdout(fie_io):
        function_name_to_be_called()
    out = fie_io.getvalue()
    return out.strip()

# Test class that implements the tests
class Test_Print_Numbers(unittest.TestCase):
    def __init__(self, methodName='', param=None):
        super(Test_Print_Numbers, self).__init__(methodName)
        self.param = param

    # Test for valid case
    def test_print_numbers_true(self):
        print(self.param)
        self.assertEqual(call_the_function(PN.print_numbers), self.param)

    # Test for invalid case
    def test_print_numbers_false(self):
        self.assertNotEqual(call_the_function(PN.print_numbers), self.param)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    test_data_true = "1,2,3,4,5,6,7,8,9,10" # test data for valid cases
    test_data_false = "2,3,4,5,6,7,8,9,10"  # test data for invalid cases
    # Test for valid case
    suite.addTest(Test_Print_Numbers("test_print_numbers_true",test_data_true))
    # Test for valid case
    suite.addTest(Test_Print_Numbers("test_print_numbers_false", test_data_false))
    runner = unittest.TextTestRunner()
    runner.run(suite)

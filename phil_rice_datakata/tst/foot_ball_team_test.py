# system imports
import unittest
import sys
import os
import io
from contextlib import redirect_stdout
import inspect
import HtmlTestRunner

# adding user import paths
program_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(program_path, "../src"))

# user imports
import process_football_team_data  # source file , for the implementation
import test_input_data # test data input

# calls the passed function and capture its out put
def call_the_function(function_name_to_be_called,arg):
    fie_io = io.StringIO()
    with redirect_stdout(fie_io):
        function_name_to_be_called(arg)
    out = fie_io.getvalue()
    return out.strip()

# Test class that implements the tests
class Test_Football_Team_data(unittest.TestCase):
    def __init__(self, methodName='', test_file_name=None , expected_out_put=None):
        super(Test_Football_Team_data, self).__init__(methodName)
        self.test_file_name = test_file_name
        self.expected_out_put = expected_out_put

    # generic test function that calls the implementation and checks the expected out put
    def test_foot_team_with_least_goal_diff(self):
        fn_name = inspect.currentframe().f_code.co_name
        print("running the function %s with parameters %s %s" %(fn_name,self.test_file_name,self.expected_out_put))
        self.assertEqual(call_the_function(process_football_team_data.print_team_least_diff_in_football_goals, self.test_file_name), self.expected_out_put)
        print("test passed")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # test the file from the https://github.com/phil-rice/datakata.git
    suite.addTest(Test_Football_Team_data("test_foot_team_with_least_goal_diff", test_input_data.test_orignal_data[0], test_input_data.test_orignal_data[1]))
    # test the empty data file
    suite.addTest(Test_Football_Team_data("test_foot_team_with_least_goal_diff", test_input_data.test_empyt_data[0], test_input_data.test_empyt_data[1]))
    # test the file with data from single team
    suite.addTest(Test_Football_Team_data("test_foot_team_with_least_goal_diff", test_input_data.test_single_data[0], test_input_data.test_single_data[1]))
    # test file with all the teams having same data , for and against goals
    suite.addTest(Test_Football_Team_data("test_foot_team_with_least_goal_diff", test_input_data.test_same_data_set[0], test_input_data.test_same_data_set[1]))
    # test file with 3 teams having same data , for and against goals
    suite.addTest(Test_Football_Team_data("test_foot_team_with_least_goal_diff", test_input_data.test_three_team_same_data_set[0], test_input_data.test_three_team_same_data_set[1]))
    # test file with one line is having valid data
    suite.addTest(Test_Football_Team_data("test_foot_team_with_least_goal_diff", test_input_data.test_one_line_valid_data[0], test_input_data.test_one_line_valid_data[1]))
    # test with invalid data
    suite.addTest(Test_Football_Team_data("test_foot_team_with_least_goal_diff", test_input_data.test_invalid_data[0],test_input_data.test_invalid_data[1]))
    # test with Zero for and Against goal
    suite.addTest(Test_Football_Team_data("test_foot_team_with_least_goal_diff", test_input_data.test_for_and_against_zero_data[0], test_input_data.test_for_and_against_zero_data[1]))
    # test with character data
    suite.addTest(Test_Football_Team_data("test_foot_team_with_least_goal_diff", test_input_data.test_with_character_data[0], test_input_data.test_with_character_data[1]))
    # test with duplicate data
    suite.addTest(Test_Football_Team_data("test_foot_team_with_least_goal_diff", test_input_data.test_with_duplicate_data[0], test_input_data.test_with_duplicate_data[1]))

    tstRepDir = os.path.join(program_path, "tst_report")
    html_runner = HtmlTestRunner.HTMLTestRunner(
        verbosity=2, output=tstRepDir,
        report_title='Test report',
        descriptions='Test report'
    )
    html_runner.run(suite)

import unittest
import os
import datetime as dt
from Utilities import HTMLTestRunner


class BaseTestSuite(object):

    @staticmethod
    def run_selected_tests(selected_tests, file_name, description):
        #   Identify the Active Directory where the Test Report is going to be created
        current_directory = (os.path.dirname(os.getcwd()))

        #   Specify the Output file for the Test Report
        outfile = open(current_directory + '\Reports\\' + file_name + '_TestReport_' +
                       dt.datetime.now().strftime("%Y-%m-%d_%H%M%S") + ".html", "w")

        #   Creating a Test Suite using the imported Test Case Files
        prepared_test_suite = unittest.TestSuite(selected_tests)

        #   Creating a runner that uses the given parameters
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title=description + ' - Test Report',
            description='Test Suite Report'
        )

        runner.run(prepared_test_suite)

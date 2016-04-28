#   This file is not yet ready

import unittest
import HTMLTestRunner
import nose
import os
import sys
sys.path.append(os.path.abspath(os.path.join(sys.path[0], os.pardir)))
from Tests import HomeBeforeLoginTests, LoginTests


# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchProductTest and HomePageTest class
home_before_login_tests = unittest.TestLoader().loadTestsFromTestCase(HomeBeforeLoginTests)

# create a test suite combining search_test and home_page_test
full_test = unittest.TestSuite([home_before_login_tests])

# open the report file
outfile = open(dir + "\FullTestReport.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report', description='System Full Test')
runner = nose.run()

# run the suite using HTMLTestRunner
runner.run(full_test)

if __name__ == '__main__':
    unittest.main()

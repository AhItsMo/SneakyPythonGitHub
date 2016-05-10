import unittest
from Tests import *

# get the directory path to output report file
# dir = os.getcwd()

# get all tests from HomeBeforeLoginTests and LoginTests classes
home_before_login_tests = unittest.TestLoader().loadTestsFromTestCase(HomeBeforeLoginTests.HomeBeforeLoginTests)
login_tests = unittest.TestLoader().loadTestsFromTestCase(LoginTests.LoginTests)

# create a test suite combining search_test and home_page_test
full_test = unittest.TestSuite([home_before_login_tests, login_tests])

# open the report file
# outfile = open(dir + "\FullTestReport.html", "w")

unittest.TextTestRunner(verbosity=2).run(full_test)

# # configure HTMLTestRunner options
# runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report', description='System Full Test')
# runner = nose.run()
#
# # run the suite using HTMLTestRunner
# runner.run(full_test)

# if __name__ == '__main__':
#     unittest.main()

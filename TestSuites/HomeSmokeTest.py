import unittest
from Tests import *
from Utilities.BaseTestSuite import BaseTestSuite

#   This list contains the desired Test Files to be executed. This is a Full Test, all files are listed.
selected_tests = [
    unittest.TestLoader().loadTestsFromTestCase(HomeBeforeLoginTests.HomeBeforeLoginTests)
    , unittest.TestLoader().loadTestsFromTestCase(HomeBeforeLoginTests.AfterLoginTests)
]

#   Description and File Name are used to customize the Test Report HTML file.
description = "Home Smoke Test"
file_name = "HomeSmokeTest"

#   Executing the listed selected tests.
BaseTestSuite.run_selected_tests(selected_tests, file_name, description)

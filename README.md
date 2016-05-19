# SneakyPythonGitHub
POC for the test automation of GitHub with Selenium WebDriver and Python

# Directories Description
- Executables: Contains .bat files that executes pre-selected tests from CMD or Windows Explorer.
- Features: Contains tests developed using BDD.
- PageObjectModels: Contains the locators and methods for the in-testing-scope pages of GitHub.
- Reports: (Ignored by Git) Contains the Execution Reports generated after running a Test Suite.
- Test Suites: Contains Test Suite files that specify which tests to run for any given Test Suite.
- Tests: Contains Test Case files for the in-testing-scope features of GitHub.
- Utilities: Contains generic files used by Tests and POMs.

# Installed packages
- selenium
- pytest-html
- pytest-capturelog
- nose
- ddt
- xlrd
- ipdb
- behave

# Installed plugins
- .ignore
- CMD Support
- Markdown support
- Gherkin

# Execution Instructions
- Option 1: Run the .bat files (in Executables directory) directly from Windows Explorer.
- Option 2: In PyCharm, right-click the .bat files (in Executables directory) and select 'Run CMD script'

# WebDriver Selection
- Change '**Driver**' value in **TestConfiguration.json** file.
- Accepted entries are: '**Firefox**' and '**Chrome**'.

# Modifications Instructions
    # Page Objects:
        - Each Page has a separate file that contains its elements locators and its methods.
        - To add more Page Objects, use **HomeBeforeLoginPage** as a reference.

    # Tests:
        - Each Test Class contains a set of test cases, _usually_ executed on the same page.
        - Each Test Case name starts with "test_xx_", where xx is an incremental counter.
        - To add more Tests, use HomeBeforeLoginTests as a referece.

    # Test Suites:
        - Add new Test Suites designed just like FullTest Test Suite.
        - Add a new Executable for the created Test Suites just like FullTestSuite.bat file.
        - No need to edit the BaseTestSuite file.
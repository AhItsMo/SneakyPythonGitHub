# SneakyPythonGitHub
POC for the test automation of GitHub with Selenium and Python

# Installed packages and plugins
- selenium
- pytest-html
- pytest-capturelog
- nose
- ddt
- .ignore
- CMD Support
- Markdown support

# Execution Instructions
- Option 1: Run the .bat files (in Executables directory) directly from Windows Explorer.
- Option 2: In PyCharm, right-click the .bat files (in Executables directory) and select 'Run CMD script'

# Modifications Instructions
    # Page Objects:
        - Each Page has a separate file that contains its elements locators and its methods

    # Tests:
        - Each Test Class contains a set of test cases, _usually_ executed on the same page
        - Each Test Case name starts with "test_xx_", where xx is an incremental counter.
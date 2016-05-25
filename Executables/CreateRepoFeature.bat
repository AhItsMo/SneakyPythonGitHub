cd..
behave --tags=CreateNewRepo
junit-viewer --results=.\Reports_JUnit\TESTS-CreateNewRepo.xml --save=.\Reports\CreateRepository_BDDTestReport_%date:~7,2%-%date:~4,2%-%date:~10,4%_%time:~0,2%%time:~3,2%%time:~6,2%.html
pause

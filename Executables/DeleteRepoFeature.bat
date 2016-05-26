cd..
behave --tags=DeleteRepo
junit-viewer --results=.\Reports_JUnit\TESTS-DeleteRepo.xml --save=.\Reports\DeleteRepository_BDDTestReport_%date:~7,2%-%date:~4,2%-%date:~10,4%_%time:~0,2%%time:~3,2%%time:~6,2%.html
pause

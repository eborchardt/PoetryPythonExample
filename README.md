![TeamCity build status](https://support-team.teamcity.com/app/rest/builds/buildType:id:Eborchardt_ServiceMessageInspections,branch:name:main/statusIcon.svg)
# A Very Basic Poetry Example
This project contains a script, main.py, which will send a TeamCity service message. There is an unused dependency on requests, which I was using only for environment verification in a test.<br>
<br>
You will need to have the following installed on your operating system:<br>
* python3
* python3-pip
* poetry
<br>

1. To use this, simply clone the repository: `git clone https://github.com/eborchardt/PoetryPythonExample.git` <br>
2. Change to the project directory: `cd PoetryPythonExample`<br>
3. Run the Poetry Install command: `poetry install`<br>
4. Run the main.py script with Poetry: `poetry run python src/someproject/main.py`<br>

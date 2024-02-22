# Use the latest windows base image
FROM mcr.microsoft.com/windows/servercore:ltsc2022

# Install Python and other dependencies
RUN powershell -Command \
    $ErrorActionPreference = 'Stop'; \
    Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe' -OutFile python_installer.exe; \
    Start-Process -FilePath 'python_installer.exe' -ArgumentList '/quiet InstallAllUsers=1 Include_test=0 PrependPath=1' -NoNewWindow -Wait; \
    Remove-Item -Path python_installer.exe -Force; \
    $env:Path = 'C:\Program Files\Python39;C:\Program Files\Python39\Scripts;' + $env:Path ; \
    python --version ; \
    pip --version ; \
    Invoke-WebRequest -Uri "https://bootstrap.pypa.io/get-pip.py" -OutFile "C:\get-pip.py" -UseBasicParsing ; \
    python C:\get-pip.py ; \
    Remove-Item C:\get-pip.py -Force ; \
    pip install poetry

# Set environment variables
RUN setx path "C:\Program Files\Python39;C:\Program Files\Python39\Scripts;%path%"
#ENV PATH="C:\Program Files\Python39;C:\Program Files\Python39\Scripts;%PATH%"

# Set up virtual environment
RUN python -m venv C:\venv

# Install any additional dependencies
RUN C:\venv\Scripts\activate && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install --upgrade poetry

# Print versions
RUN python --version && \
    pip --version && \
    poetry --version

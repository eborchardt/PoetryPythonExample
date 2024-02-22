FROM python:3.12.2-windowsservercore

# Set execution policy for script execution (use with caution)
RUN powershell.exe Set-ExecutionPolicy Bypass -Scope CurrentUser -Force

# Install prerequisites
RUN choco install pythontools -y

# Download and install Poetry
RUN curl -sSL https://install.python-poetry.org | powershell.exe -ExecutionPolicy Bypass -NoProfile -NonInteractive

# Install teamcity-messages
RUN poetry install teamcity-messages

# Clean up
RUN rm -rf /var/cache/chocolatey

# Make Poetry and teamcity-messages available
WORKDIR /usr/local/bin
COPY poetry poetry
COPY teamcity-messages teamcity-messages

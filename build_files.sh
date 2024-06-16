#!/bin/bash

# Ensure Python 3.9 and pip are available
PYTHON_VERSION=python3.9
PIP=pip

# Install dependencies from requirements.txt
$PIP install -r requirements.txt

# Collect static files (adjust settings as needed)
$PYTHON_VERSION manage.py collectstatic --noinput

# Additional build steps if needed
# e.g., migrate database
$PYTHON_VERSION manage.py migrate

# Start the Django server or any other necessary command
$PYTHON_VERSION manage.py runserver

#!/bin/bash
# build_files.sh
echo "Building the project..."
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput
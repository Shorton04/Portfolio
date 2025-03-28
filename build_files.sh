#!/bin/bash
# vercel.build.sh
export PATH=$PATH:/vercel/.local/bin
pip install -r requirements.txt
python manage.py collectstatic --noinput
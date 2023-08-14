#!/bin/bash

# exit on error
set -o errexit

touch /var/log/python.log
ln -s /usr/bin/python3 /usr/bin/python
python --version > /var/log/python.log
cat /var/log/python.log

python manage.py collectstatic --no-input
python manage.py migrate

apache2ctl -D FOREGROUND

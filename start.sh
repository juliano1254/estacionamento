#!/bin/bash

# exit on error
set -o errexit

FILE=/etc/secrets/.env
if test -f "$FILE"; then
    echo "$FILE existe."
    ln -s /etc/secrets/.env /var/www/html/
    chmod +r /var/www/html/.env
fi

touch /var/log/python.log
ln -s /usr/bin/python3 /usr/bin/python
python --version > /var/log/python.log
cat /var/log/python.log

python manage.py collectstatic --no-input
python manage.py migrate

apache2ctl -D FOREGROUND &
tail -f /var/log/apache2/error.log
#!/bin/bash

# exit on error
set -o errexit

FILE=/etc/secrets/.env
if test -f "$FILE"; then
    echo "$FILE existe."
    cp /etc/secrets/.env /var/www/html/
    chown www-data: /var/www/html/.env
    chmod +r /var/www/html/.env
fi

touch /var/log/python.log
ln -s /usr/bin/python3 /usr/bin/python
python --version > /var/log/python.log
cat /var/log/python.log

python manage.py collectstatic --no-input
## CRIANDO O BANCO DE DADOS
python manage.py makemigrations
python manage.py migrate

## Criando o super usuário
#if $CREATE_SUPERUSER;
if false;
then
    echo $CREATE_SUPERUSER
    python /var/www/html/manage.py createsuperuser --no-input
else
    echo "Superuser já existe!"
fi

apache2ctl -D FOREGROUND &
tail -f /var/log/apache2/error.log
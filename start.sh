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
./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin_j', 'juliano1254@gmail.com', '4v;O;<TM4Utkj?61vV:b')"


apache2ctl -D FOREGROUND &
tail -f /var/log/apache2/error.log
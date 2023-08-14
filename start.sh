#!/bin/bash

touch /var/log/python.log
ln -s /usr/bin/python3 /usr/bin/python
python --version > /var/log/python.log
cat /var/log/python.log
apache2ctl -D FOREGROUND


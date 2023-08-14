FROM ubuntu:lunar

WORKDIR /var/www/html

EXPOSE 80

RUN apt-get update && \
    apt-get install -y apache2 && \
    apt-get install -y python3 && \
    apt-get install -y python3-django && \
    apt-get install -y python3-dj-database-url && \
    apt-get install -y python3-dj-static && \
    apt-get install -y python3-decouple && \
    apt-get install libapache2-mod-wsgi-py3 -y

RUN mkdir -p /var/www/html/estacionamento && \
    mkdir -p /var/www/html/core/templates/core && \
    mkdir -p /var/www/html/templates

## CONFIGURAÇÕES DO CONTAINER
COPY apache2.conf /etc/apache2/
COPY 000-default.conf /etc/apache2/sites-enabled/
#COPY index.html /var/www/html/
COPY start.sh /var/

## COPIANDO O SISTEMA
COPY core/ /var/www/html/core
COPY core/templates/core /var/www/html/core/templates/core/
COPY estacionamento/ /var/www/html/estacionamento/
COPY templates/ /var/www/html/templates/
COPY manage.py /var/www/html/
#COPY .env /var/www/html/

ENTRYPOINT chmod +x /var/start.sh && /var/start.sh

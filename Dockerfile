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
    apt-get install libapache2-mod-wsgi-py3 -y && \
    apt-get install python3-psycopg2 -y && \
    apt-get install python3-django-bootstrapform && \
    apt-get clean

RUN mkdir -p /var/www/html/estacionamento && \
    mkdir -p /var/www/html/core/templates/core && \
    mkdir -p /var/www/html/templates && \
    mkdir -p /var/www/html/static/css && \
    mkdir -p /var/www/html/website

## CONFIGURAÇÕES DO CONTAINER
COPY apache2.conf /etc/apache2/
COPY 000-default.conf /etc/apache2/sites-enabled/
COPY start.sh /var/

## COPIANDO O SISTEMA
COPY core/ /var/www/html/core
COPY core/templates/core /var/www/html/core/templates/core/
COPY estacionamento/ /var/www/html/estacionamento/
COPY templates/ /var/www/html/templates/
COPY manage.py /var/www/html/
COPY static/css/ /var/www/html/static/css/
COPY static/js/ /var/www/html/static/js/
COPY website/ /var/www/html/website/
#COPY index.html /var/www/html/
#COPY .env /var/www/html/

ENTRYPOINT chmod +x /var/start.sh && /var/start.sh

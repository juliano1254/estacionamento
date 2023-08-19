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
    apt-get install -y libapache2-mod-wsgi-py3 && \
    apt-get install -y python3-psycopg2 && \
    apt-get install -y python3-django-bootstrapform && \
#    apt-get install -y python-xhtml2pdf && \
    apt-get clean

RUN mkdir -p /var/www/html/estacionamento


## CONFIGURAÇÕES DO CONTAINER
COPY apache2.conf /etc/apache2/
COPY 000-default.conf /etc/apache2/sites-enabled/
COPY start.sh /var/

## COPIANDO O SISTEMA
COPY core/ /var/www/html/core/
COPY estacionamento/ /var/www/html/estacionamento/
COPY templates/ /var/www/html/templates/
COPY manage.py /var/www/html/
COPY static/ /var/www/html/static/
COPY website/ /var/www/html/website/
#COPY .env /var/www/html/

ENTRYPOINT chmod +x /var/start.sh && /var/start.sh

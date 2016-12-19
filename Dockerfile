FROM ubuntu:xenial

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    build-essential \
    ca-certificates \
    gcc \
    libpq-dev \
    make \
    pkg-config \
    nginx \
    python3 \
    python3-dev \
    python3-venv \
    python3-pip \
    supervisor \
    postgresql-client \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


RUN ln -s /usr/bin/python3 /usr/local/bin/python && \
    ln -s /usr/bin/pip3 /usr/local/bin/pip

ADD ./requirements.txt /src/requirements.txt

RUN pip install pip --upgrade && \
    pip install -r /src/requirements/common.txt && \
    pip install uwsgi==2.0.14

ADD . /src

RUN mkdir -p /var/log/uwsgi && \
    mkdir -p /usr/local/etc/uwsgi

COPY server-configs/supervisor.conf /etc/supervisor/supervisord.conf
COPY server-configs/supervisor-app.conf /etc/supervisor/conf.d/supervisor-app.conf
COPY server-configs/uwsgi-app.ini /usr/local/etc/uwsgi/uwsgi-app.ini
COPY server-configs/nginx-app.conf /etc/nginx/sites-available/nginx-app.conf
RUN ln -s /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx-app.conf
RUN rm /etc/nginx/sites-enabled/default


EXPOSE 80
 
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

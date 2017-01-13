FROM xxxxx.dkr.ecr.ap-northeast-1.amazonaws.com/api-server-base:latest

ADD . /src

COPY server-configs/supervisor.conf /etc/supervisor/supervisord.conf
COPY server-configs/supervisor-app.conf /etc/supervisor/conf.d/supervisor-app.conf
COPY server-configs/uwsgi-app.ini /usr/local/etc/uwsgi/uwsgi-app.ini
COPY server-configs/nginx-app.conf /etc/nginx/sites-available/nginx-app.conf
RUN ln -s /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx-app.conf
RUN rm /etc/nginx/sites-enabled/default

EXPOSE 80
 
# CMD ["/bin/bash"]
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

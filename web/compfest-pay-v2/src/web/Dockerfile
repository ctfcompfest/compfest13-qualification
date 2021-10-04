FROM nginx:alpine

RUN apk update && apk upgrade
RUN apk --no-cache add python3 \
    py3-greenlet py3-gevent py3-gunicorn py3-pillow

COPY docker .
RUN apk --no-cache add py3-pip python3-dev && \
    pip3 install -r server-req.txt && rm server-req.txt && \
    apk del py3-pip python3-dev
RUN chmod +x *.sh && \
    mv nginx.conf /etc/nginx/nginx.conf

ENV POSTGRES_USER=postgres POSTGRES_PASSWORD=SemogaPa55word1ni4man
RUN /postgres-alpine.sh

WORKDIR /opt/ctf/app
COPY server .

RUN apk --no-cache add python3-dev py3-pip postgresql-dev musl-dev build-base zlib-dev jpeg-dev freetype-dev && \
    pip3 install --ignore-installed --no-cache-dir -r requirements.txt && \
    apk del python3-dev py3-pip postgresql-dev musl-dev build-base zlib-dev jpeg-dev freetype-dev

RUN python3 manage.py collectstatic && \
    python3 manage.py makemigrations

ENV PRODUCTION=true
ENV GUNICORN_WSGI_MODULE=compfestpay2.wsgi:application
ENV GUNICORN_NAME=ctf GUNICORN_SOCKFILE=/run/gunicorn.sock
ENV GUNICORN_USER=nobody GUNICORN_GROUP=nobody

CMD ["/entrypoint.sh"]

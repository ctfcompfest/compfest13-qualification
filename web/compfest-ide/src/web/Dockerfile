FROM nginx:alpine

RUN apk update && apk upgrade
RUN apk --no-cache add python3 \
    py3-greenlet py3-gevent py3-gunicorn

COPY docker .
RUN apk --no-cache add --virtual build-dep py3-pip python3-dev && \
    pip3 install --no-cache-dir -r server-req.txt && rm server-req.txt && \
    apk del build-dep
RUN chmod +x *.sh && \
    mv nginx.conf /etc/nginx/nginx.conf

ENV POSTGRES_USER=postgres POSTGRES_PASSWORD=4noTh3rPassw0rdisHard
RUN /postgres-alpine.sh

WORKDIR /opt/ctf/app
COPY server/requirements.txt .

RUN apk --no-cache add --virtual build-dep python3-dev py3-pip postgresql-dev musl-dev gcc && \
    pip3 install --no-cache-dir -r requirements.txt && \
    apk del build-dep

COPY server .
RUN python3 manage.py makemigrations

ENV CODE_DIR=/compfestide/code SANDBOX_DIR=/compfestide/sandbox

# Setting machine for safely execute user input
RUN mkdir -p ${CODE_DIR}
RUN mkdir -p ${SANDBOX_DIR}/lib/usr && \
    cp -R /lib* ${SANDBOX_DIR} && \
    cp -R /usr/lib* ${SANDBOX_DIR}/usr/
RUN mkdir -p ${SANDBOX_DIR}/bin && \
    cp /bin/sh ${SANDBOX_DIR}/bin/sh && \
    cp /bin/ls ${SANDBOX_DIR}/bin/ls && \
    cp /bin/cat ${SANDBOX_DIR}/bin/cat && \
    cp /bin/echo ${SANDBOX_DIR}/bin/echo
RUN mv flag.txt ${SANDBOX_DIR}/PR1ze

RUN chmod 777 ${SANDBOX_DIR}
RUN chmod 777 ${CODE_DIR}

ENV PRODUCTION=true
ENV GUNICORN_WSGI_MODULE=compfestide.wsgi:application
ENV GUNICORN_NAME=ctf GUNICORN_SOCKFILE=/run/gunicorn.sock
ENV GUNICORN_USER=nobody GUNICORN_GROUP=nobody

CMD ["/entrypoint.sh"]

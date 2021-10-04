FROM nginx:alpine

RUN apk update && apk upgrade
RUN apk add --no-cache --update nodejs npm
RUN npm install pm2@latest -g

COPY src/web/docker .
RUN chmod +x *.sh && \
    mv nginx.conf /etc/nginx/nginx.conf 

WORKDIR /opt/ctf/app
COPY src/web/server/package.json .
RUN npm install

COPY src/web/server .

ENV PRODUCTION=true NUM_WORKER=4 
ENV MAIN_APP=index.js

CMD [ "/entrypoint.sh" ]
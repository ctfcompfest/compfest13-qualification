FROM python:slim-buster

RUN apt-get update && \
    apt-get install -y lib32z1 xinetd --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m ctf
WORKDIR /home/ctf

RUN mkdir -p usr/local && \
    cp -R /lib* /home/ctf && \
    cp -R /usr/lib* /home/ctf/usr && \
    cp -R /usr/local/lib* /home/ctf/usr/local

RUN mkdir /home/ctf/dev && \
    mknod /home/ctf/dev/null c 1 3 && \
    mknod /home/ctf/dev/zero c 1 5 && \
    mknod /home/ctf/dev/random c 1 8 && \
    mknod /home/ctf/dev/urandom c 1 9 && \
    chmod 666 /home/ctf/dev/*

RUN mkdir /home/ctf/bin && \
    cp /bin/sh /home/ctf/bin && \
    cp /bin/ls /home/ctf/bin && \
    cp /bin/cat /home/ctf/bin && \
    cp /bin/echo /home/ctf/bin && \
	cp /usr/bin/expr /home/ctf/bin

RUN cp /usr/local/bin/python* /home/ctf/bin

COPY ./docker /
RUN chmod +x /*.sh && \
    mv /run.sh . && \
    mv /xinetd.conf /etc/xinetd.conf

RUN mv /alice.xinetd /etc/xinetd.d/alice && \
    mv /alicebob.xinetd /etc/xinetd.d/alicebob && \
    mv /bob.xinetd /etc/xinetd.d/bob

COPY ./server .
RUN chmod 444 secrets.py && \
    chmod 555 alice-bob.py && \
    chmod 555 chats.py && \
    chmod 555 talk-with-alice.py && \
    chmod 555 talk-with-bob.py

RUN [ -f requirements.txt ] && \
    pip3 install -r requirements.txt && \
    cp -R /usr/local/lib/python* /home/ctf/usr/local/lib/ || exit 0

RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail

EXPOSE 9990
EXPOSE 9991
EXPOSE 9992

CMD ["/start.sh"]

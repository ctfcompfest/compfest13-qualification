# Writeup VidCap

*From https://github.com/quo/rtmp2flv*
```bash
#Requries tcpflow
sudo apt-get install tcpflow
tcpflow -T %T_%A%C%c.rtmp -r *.pcapng
./rtmp2flv.py *.rtmp
#Open the .flv file
```
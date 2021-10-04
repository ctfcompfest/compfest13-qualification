# Writeup FIrewall-ed

- Reorder packet using `reodercap`
- Retrieve Filtered-port packet in order to retrieve 2-byte of content file. Got flag.zip and password 
- Unzip flag.zip using given password

```sh
$ reordercap network_log.pcap log.pcap
$ python2 sv.py
```
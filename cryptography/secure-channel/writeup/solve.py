#!/usr/bin/env python3
from base64 import b64encode, b64decode, a85decode
from Crypto.Util.number import long_to_bytes as lb, bytes_to_long as bl
from Crypto.Cipher import AES
from pwn import *
import libnum
import string

# get the message from alice-bob conversation
alice_bob = process('../src/alice-bob.py')
payload = b64encode(lb(0x100000000000000000000000000000000)) # g
alice_bob.recvuntil(b'g: ')
alice_bob.sendline(payload)

alice_dialogue = []
bob_dialogue = []
res = alice_bob.recvuntil(b'Message received!\n').split(b'\n\n')

parse = res[0].split(b'\n')
prime_p = int(parse[0][3:].decode())
ga_mod_p = parse[1][21:]

alice_dialogue.append(res[1].split(b'\n')[1])
res = alice_bob.recvuntil(b'Message received!\n').split(b'\n')[2]
bob_dialogue.append(res)
MESSAGE_COUNT = 12
for i in range(MESSAGE_COUNT):
    res = alice_bob.recvuntil(b'Message received!\n').split(b'\n')[2]
    alice_dialogue.append(res)
    res = alice_bob.recvuntil(b'Message received!\n').split(b'\n')[2]
    bob_dialogue.append(res)
alice_dialogue = list(map(b64decode, alice_dialogue))
bob_dialogue = list(map(b64decode, bob_dialogue))
print('alice_dialogue =', alice_dialogue)
print('bob_dialogue =', bob_dialogue)
print('prime_p =', prime_p)
print('ga_mod_p =', ga_mod_p)

alice_bob.close()


def solution1():
    # talk with bob several times to get pow(g, ALICE * BOB, some prime), we set the g as pow(g, ALICE, prime_p)
    # how many times we should talk with bob? we need to do that a certain amount so pow(ga_mod_p, bob.key) < multiple of all primes when we connect to Bob
    primes = []
    gab_mod_primes = []
    TALK_WITH_BOB = 100
    for i in range(TALK_WITH_BOB):
        bob = process('../src/talk-with-bob.py')

        bob.recvuntil(b'Your secret: ')
        payload = b64encode(lb(1))
        bob.sendline(payload)

        bob.recvuntil(b'g: ')
        payload = ga_mod_p
        bob.sendline(payload)

        res = bob.recvuntil(b'Message to Bob:').split(b'\n')
        primes.append(int(res[0][3:].decode()))
        gab_mod_primes.append(bl(b64decode(res[1][19:])))
        bob.close()    

    print('gab_mod_primes =', gab_mod_primes)
    print('primes =', primes)

    # get pow(g, ALICE * BOB, prime_p) from CRT, get key
    
    return libnum.solve_crt(gab_mod_primes, primes) % prime_p

def solution2():
    # bruteforce to get gab_mod_p
    bob = process('../src/talk-with-bob.py')

    bob.recvuntil(b'Your secret: ')
    payload = b64encode(lb(1))
    bob.sendline(payload)

    bob.recvuntil(b'g: ')
    payload = b64encode(lb(0x100000000000000000000000000000000)) # g
    bob.sendline(payload)

    res = bob.recvuntil(b'Message to Bob:').split(b'\n')
    bob.close()
    primes = int(res[0][3:].decode())
    gab_mod_primes = bl(b64decode(res[1][19:]))
    forge_g = 0x100000000000000000000000000000000
    tmp = forge_g % primes
    bob_key = 1
    while forge_g != gab_mod_primes:
        forge_g *= tmp
        forge_g %= primes
        bob_key += 1
    return pow(bl(b64decode(ga_mod_p)), bob_key, prime_p)

gab_mod_p = solution2() #solution1()
print('gab_mod_p =', gab_mod_p)
print()

key = gab_mod_p % 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
key = lb(key)
while (len(key) != 16):
    key += b'\x01'
print('key:', key, bl(key))

# profit
sp = list(map(ord, list(string.printable)))
def unpad(msg):
    new_msg = []
    for c in msg:
        if (c in sp):
            new_msg.append(c)
    return bytearray(new_msg)

def decrypt_message(enc_message):
    global key
    iv = enc_message[:16]
    enc = enc_message[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    msg = cipher.decrypt(enc)
    return a85decode(unpad(msg))

for i in range(len(alice_dialogue)):
    print('Alice:', decrypt_message(alice_dialogue[i]).decode())
    print('Bob:', decrypt_message(bob_dialogue[i]).decode())

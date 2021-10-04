from pwn import *
from Crypto.Util.number import long_to_bytes as lb, bytes_to_long as bl
from binascii import unhexlify as uhy, hexlify as hy
from Crypto.Cipher import AES

LOCAL = 1
if LOCAL:
    p = process('../src/server/chall.py')
else:
    p = remote('localhost', 2000)

def get_flag():
    p.sendlineafter(b'> ', b'1')
    return p.recvuntil(b'\n')[16:-1]

def encrypt(msg):
    p.sendlineafter(b'> ', b'2')
    p.sendlineafter(b'msg (in hex) = ', msg)
    return p.recvuntil(b'\n')[15:-1]


def decrypt(enc):
    p.sendlineafter(b'> ', b'3')
    p.sendlineafter(b'enc (in hex) = ', enc)
    return p.recvuntil(b'\n')[15:-1]

def unpad(msg):
    return msg[:-msg[-1]]

enc_flag = get_flag()
dec_flag = decrypt(enc_flag)

i = 0
c1 = bl(uhy(enc_flag[32*i:32*(i+1)]))
m1 = bl(uhy(dec_flag[32*i:32*(i+1)]))
m1_xor_c1 = m1 ^ c1

i = 1
c2 = bl(uhy(enc_flag[32*i:32*(i+1)]))
dec_c2 = bl(uhy(decrypt(hy(lb(c2)))))

m2_xor_iv = dec_c2 ^ m1_xor_c1
F_m2 = bl(uhy(encrypt(hy(lb(m2_xor_iv)))[:32]))
F__F_m2_xor_m1_ = bl(uhy(encrypt(hy(lb(m2_xor_iv)) + hy(lb(m1)))[32:64]))
F_m2_xor_m1_xor_iv = bl(uhy(decrypt(hy(lb(F__F_m2_xor_m1_)))))
iv = F_m2_xor_m1_xor_iv ^ m1 ^ F_m2
m2 = dec_c2 ^ iv ^ m1_xor_c1

flag = lb(m1) + lb(m2)
for i in range(2, len(enc_flag) // 32):
    enc = enc_flag[32*i:32*(i+1)]
    msg = bl(uhy(decrypt(enc)))
    c_i_before = bl(uhy(enc_flag[32*(i-1):32*i]))
    m_i_before = bl(flag[16*(i-1):16*i])
    m_i = msg ^ iv ^ m_i_before ^ c_i_before
    flag += lb(m_i)

flag = unpad(flag)
cipher = AES.new(lb(iv), AES.MODE_ECB)
flag = cipher.decrypt(flag)

print('FLAG =', unpad(flag).decode())

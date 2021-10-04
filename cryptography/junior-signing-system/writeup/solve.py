# this part of solver is to find matrix A to later generate lattice L
# see the 2nd paper for details

from pwn import *
from collections import namedtuple
from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes
from Crypto.Hash import SHA1
import os

def add(first, second):
    global p
    return ((first % p) + (second % p)) % p

def subtract(first, second):
    global p
    return (first % p - second % p + p) % p

def multiply(first, second):
    global p
    return ((first % p) * (second % p)) % p

def divide(first, second):
    global p
    return multiply(first, inverse(second, p))

def negative(P):
    return Point(P.x, subtract(0, P.y))

def point_addition(P, Q):
    global p, a

    if (P.x == 0 and P.y == 0):
        return Q
    if (Q.x == 0 and Q.y == 0):
        return P
    
    x1, y1, x2, y2 = P.x, P.y, Q.x, Q.y
    
    if (x1 == x2 and (y1 + y2) % p == 0):
        return Point(0, 0)
    
    if (x1 != x2 or y1 != y2):
        res = divide(subtract(y2, y1), subtract(x2, x1))
    else:
        res = divide(add(multiply(3, multiply(x1, x1)), a), multiply(2, y1))
    
    x3 = subtract(subtract(multiply(res, res), x1), x2)
    y3 = subtract(multiply(res, subtract(x1, x3)), y1)
    return Point(x3, y3)

def scalar_multiplication(k, P):
    global Point

    Q = Point(0, 0)
    k = bin(k)[2:]
    
    for k_i in k:
        Q = point_addition(Q, Q)
        if (k_i == '1'):
            Q = point_addition(Q, P)
        
    return Q

# constants
Point = namedtuple('Point', 'x y')
p = 0xE95E4A5F737059DC60DFC7AD95B3D8139515620F
a = 0x340E7BE2A280EB74E2BE61BADA745D97E8F7C300
b = 0x1E589A8595423412134FAA2DBDEC95C8D8675E58
assert 4 * (a ** 3) + 27 * (b ** 2) != 0
E = lambda x : (x**3 + a*x + b) % p
x = 0xBED5AF16EA3F6A4F62938C4631EB5AF7BDBCDBC3
y = 0x1667CB477A1A8EC338F94741669C976316DA6321
n = 0xE95E4A5F737059DC60DF5991D45029409E60FC09
P = Point(x, y)
Q = Point(800275427720922557555616466870365302396656183171, 882672591994607972704810179243683754115208179489)
message = 'aaa'
message = message.encode()
hash = SHA1.new()
hash.update(message)
hash = bytes_to_long(hash.digest()) % n

sh = remote('localhost', 3001)#process('../src/chall.py')

k_gamma_delta = []
signature_cnt = 16 # this will do, smaller signatures count maybe can do too
special_list = []

for i in range(signature_cnt):
    sh.recvuntil(b'> ')
    sh.sendline(b'1')
    sh.recvuntil(b'Your message: ')
    sh.sendline(message)
    sh.recvuntil(b'Want to try the special feature? (y/n): ')
    sh.sendline(b'y')
    sh.recvuntil(b'Your special: ')
    special_list.append(eval(sh.recvuntil(b')')))
sh.close()

for i in range(signature_cnt):
    print('signature %d' % i)
    gamma_i, delta_i, delta = special_list[i]
    '''
    #search y of a point with known x in ecc with sage:
    #https://stackoverflow.com/questions/11043648/calculate-the-y-coordinate-of-a-point-of-a-elliptic-curve-with-sage
    #I don't have sagemath locally :v, so I should do this manually using https://sagecell.sagemath.org/
    p = ?
    a = ?
    b = ?
    gamma = ?
    E=EllipticCurve(GF(p),[a,b])
    print(str(E.lift_x(gamma)).split(' : ')[1]) # y
    '''
    T_i = Point(gamma_i, int(input('x = %d\ny = ' % gamma_i).strip()))
    two_times_T_i = point_addition(T_i, T_i)

    w = inverse(delta_i, n)
    u1 = (hash * w) % n
    u2 = (gamma_i * w) % n
    T = point_addition(scalar_multiplication(u1, P), scalar_multiplication(u2, Q))
    gamma = T.x % n
    k_bar_dot_P_1 = point_addition(scalar_multiplication(2, T_i), negative(T))
    k_bar_dot_P_2 = point_addition(scalar_multiplication(2, negative(T_i)), negative(T))

    k_bar_dot_P_tmp = Point(0, 0)
    k_bar = 0
    while True:
        k_bar_dot_P_tmp = point_addition(k_bar_dot_P_tmp, P)
        k_bar += 1
        if (k_bar_dot_P_tmp.x == k_bar_dot_P_1.x or k_bar_dot_P_tmp.x == k_bar_dot_P_2.x):
            break

    k_gamma_delta.append((k_bar, gamma, delta))
    print()

k_list = []
s_list = []
t_list = []
gamma_list = []
delta_list = []
k_list.append(k_gamma_delta[0][0])
gamma_list.append(k_gamma_delta[0][1])
delta_list.append(k_gamma_delta[0][2])
k_0 = k_gamma_delta[0][0]
gamma_0 = k_gamma_delta[0][1]
delta_0 = k_gamma_delta[0][2]
two_power_to_length_of_k_0 = 1<<(max(len(bin(k_0)) - 2, 12))
for i in range(1, signature_cnt):
    k_i = k_gamma_delta[i][0]
    gamma_i = k_gamma_delta[i][1]
    delta_i = k_gamma_delta[i][2]
    two_power_to_length_of_k_i = 1<<(max(len(bin(k_i)) - 2, 12))

    A_i = (- (gamma_i * inverse(delta_i, n)) * (delta_0 * inverse(gamma_0, n))) % n
    B_i = ((gamma_i * inverse(delta_i, n)) * (hash * inverse(gamma_0, n)) - (hash * inverse(delta_i, n))) % n
    
    k_list.append(k_i)
    gamma_list.append(gamma_i)
    delta_list.append(delta_i)
    s_list.append((A_i * two_power_to_length_of_k_0 * inverse(two_power_to_length_of_k_i, n)) % n)
    t_list.append(((k_i + A_i * k_0 + B_i) * inverse(two_power_to_length_of_k_i, n)) % n)

print('s_list =', s_list)
print('t_list =', t_list)
print('k_list =', k_list)
print('gamma_list =', gamma_list)
print('delta_list =', delta_list)

matrix = []
matrix.append([-1] + s_list)
for i in range(1, signature_cnt):
    tmp = [0 for j in range(signature_cnt)]
    tmp[i] = n
    matrix.append(tmp)
t = [0] + t_list

gg = open('matrix', 'w')
gg.write('[')
for row in matrix:
    gg.write('[' + ' '.join(list(map(str, row))) + ']')
gg.write(']')
gg.write('[' + ' '.join(list(map(str, [0] + t_list))) + ']')
gg.close()

# we can use https://github.com/fplll/fplll for CVP
# read the paper for details why we need CVP
res = os.popen('fplll -a cvp matrix').read()
os.system('rm matrix')
res = res.strip()[1:-1].split(' ')
res = list(map(int, res))

i = 0
k_i = k_list[i]
two_power_to_length_of_k_i = 1<<(max(len(bin(k_i)) - 2, 12))
z_i = res[i] - t[i]
k = k_i + two_power_to_length_of_k_i * z_i
gamma = gamma_list[i]
delta = delta_list[i]
d = (hash - delta * k) * inverse(-1 * gamma, n)
d %= n
print('d =', d)
print('long_to_bytes(d) =', long_to_bytes(d))
print()

flag = long_to_bytes(d).decode()
formatted_flag = 'COMPFEST13{%s}' % flag
print('FLAG =', formatted_flag)
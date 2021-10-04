from base64 import a85encode

FLAG = "COMPFEST13{bRutefoRc3_1s_e4zY_Af_6965d74c2e}"
FLAG = FLAG + " " * (4 - len(FLAG) % 4)
GESER = 166
FLAG85 = a85encode(FLAG.encode()).decode()
cipher = [ord(e) + GESER for e in FLAG85]
cipher_bin = [bin(e)[2:].rjust(9, '0') for e in cipher]

tmp = str(list(''.join(cipher_bin))).replace('\'', '')[1:-1]
print(tmp)
flag_bytes = '1f43943fda1fb692b6805349836cb5f78ecc2dbd59aff818ce39c8c4e7e8d569f78a9c092d0a8dbcb4829778b4ac4df758090ab8ae99f913113ddbdee8d9c06fd17d9b01fbeb8780488c7f496863b71e68f9da8346adfed5090ff8dd37f2dc7bed5d'

out = ''

# Little endian converter
def le(string):
    string = string[::-1]
    out = [''] * len(string)
    for i in range(len(string)):
        if(i % 2 == 0):
            out[i + 1] = string[i]
        else:
            out[i - 1] = string[i]
    return "".join(out)
    
flag = le(flag_bytes)
state = 0x42
print(f"Converted flag: {flag}\n")

for i in range(0x62):
    for j in range(0, 0x100):
        if(((j + 0x13) % 0x100) ^ ((state - 0x37) % 0x100) == int(flag[i*2:i*2+2], 0x10)):
            out += chr(j)
            state *= 3
            break
            
print(out)

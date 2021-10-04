from random import shuffle, choice
import string
import os

def get_random_string(n):
    hrf = string.ascii_letters + string.punctuation + string.digits + " "
    hrf = hrf.replace("\\", "").replace("\"", "")
    return "".join([choice(hrf) for _ in range(n)])

def get_class_code(n, c, nxt):
    if nxt == None:
        last = "System.out.println(\"\\nDone!\");"
    else:
        last = "c" + str(nxt) + ".pave(flag);"
    return """class c""" + str(n) +""" {
    public static void main(String[] args) throws Exception {
        System.out.print("Paving your way.");
        c""" + str(n) +""".pave("");
    }
    public static void pave(String flag) throws Exception {
        flag = flag + \"""" + c + """\";
        System.out.print(".");
        Thread.sleep(3600000);
        """ + last + """
    }
}\n"""

def get_manifest_file(n):
    with open("source.mf", "w") as file:
        file.write("Manifest-Version: 1.0\n")
        file.write(f"Main-Class: c{n}\n")

def generate_bundle_code(s, cnt, code):
    for i in range(len(s)):
        c = s[i]
        if i == len(s) - 1: nxt = None
        else: nxt = num[cnt + 1]
        code[num[cnt]] = get_class_code(num[cnt], c, nxt)
        cnt += 1
    return cnt

def compile_code():
    os.system("javac source.java")
    os.system("jar cmf source.mf chall.jar *.class")
    os.system("rm *.class")

#
# MAIN PROGRAM
#

FLAG = "COMPFEST13{WhaY_j4r_ne3d_MaNiFeSt_file_oOf_bafc2b182e}"
NOISE = [
    "COMPFEST13{" + get_random_string(23) + ")",
    "compfest12{" + get_random_string(30) + "}",
    "COMPFEST14{kami_tunggu_partisipasi_tahun_depan}",
    "COMPFEST13[ini_bukan_flag_asli_serius]",
    "C0MPFEST13(saya_harap_kalian_jujur)",
    get_random_string(35),
    get_random_string(25),
    "COMPFEST12{terimakasih_atas_partisipasinya}",
    "COMPFEST13_ayo_jujur_dan_tidak_merusak_server",
    get_random_string(25) * 4,
    "COMPFEST" + get_random_string(30),
    "COMPFEST" + get_random_string(30),
    "COMPFEST" + get_random_string(30),
    "COMPFEST" + get_random_string(30),
    "cOmPFeST" + get_random_string(30),
    get_random_string(30) * 10,
    "THANK YOU!"
]

total_len = len(FLAG)
for e in NOISE:
    total_len += len(e)
print(total_len)
num = [i for i in range(total_len)]
shuffle(num)
shuffle(num)

code = ["" for _ in range(total_len)]

cnt = generate_bundle_code(FLAG, 0, code)
for e in NOISE:
    cnt = generate_bundle_code(e, cnt, code)

get_manifest_file(num[0])
with open('source.java', 'w') as file:
    for e in code:
        file.write(e)
compile_code()
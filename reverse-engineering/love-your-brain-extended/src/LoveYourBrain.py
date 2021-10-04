FLAG = "COMPFEST13{Y0u_607_17_60d4Mm17_1M_Pr0Ud_0f_y0U_N0W_74K3_R357_cda9bb35f3}"
FAIL_STR = "Lol sorry, wrong flag, try again. Or not? idk :)"
SUCCESS_STR = "Nice! You got it!"

def print_brainfuck(txt):
    BF_PRINT_CLEAN = "->++++++++++[>#DIV#+[-<+]->-]>#MOD#+[-<+]>>[.[-]>]"

    lst = list(txt)
    div_lst = [ord(x) // 10 for x in lst]
    mod_lst = [ord(x) % 10 for x in lst]
    DIV = '>'.join(['+'*i for i in div_lst])
    MOD = '>'.join(['+'*i for i in mod_lst])
    tmp = BF_PRINT_CLEAN.replace('#DIV#',DIV)
    tmp2 = tmp.replace('#MOD#',MOD)
    return tmp2

def hush(txt):
    return [(max(ord(x)-32,0)+47)%94 for x in txt]

def minify(txt):
    import re
    return "".join(re.findall("""([+\-[\].,><]+)""", txt))

def boxify(txt):
    tmp = ""
    for i in range(len(txt)):
        if (i % 80 == 0):
            tmp += '\n' + txt[i]
        else:
            tmp += txt[i]
    return tmp[1:]


strings =  """
Mark start of string
>-

Input until new line or null
>>>>>,[----------[++++++++++>>>>>,>]<]

Mark end of string
>---<

Back to start of string
+[-<+]-


max of (ord(char_i) minus 32) and 0 plus 47 mod 94
>>>>>[

    layout: 0 0 0 i n temp0 temp1 0 0 n_iplus1 0 0 0 0

    Initialize i to 32
    <++++++++++++++++++++++++++++++++

    Decrement loop: result is max of n minus 32 and 0
    [
        Setup temp0
        >>[-]+

        Setup temp1
        >[-]

        Back to n
        <<

        Decrement n and i
        -<-

        Back to n
        >

        If n is not null then continue
        [>-]

        Else empty i
        >[- <<[-]>> >]

        assert i
        <<<
    ]

    Modulus
    n >+++++++++++++++++++++++++++++++++++++++++++++++
    d >++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    <

    0 n(pointer here) d 0 0 0
    [>->+<[>]>[<+>-]<<[<]>-]

    >[-]

    >[-<<+>>]

    Go to next n
    >>>
]

Back to start
+[-<+]-
"""

for char in hush(FLAG):
    strings += f">>>>>{'-'*char}[[-]--+[-<+]-<[-]+>++[-->++]]\n"

strings += "+[-<+]-\n"
strings += ">+++[[-]>+++]\n"
strings += "+[-<+]-\n"

strings += f"""
<[->[-]< {print_brainfuck(FAIL_STR)} ]

>[[-]< {print_brainfuck(SUCCESS_STR)}]
"""

print(boxify(minify(strings)))
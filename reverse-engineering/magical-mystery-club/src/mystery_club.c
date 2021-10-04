#include<stdio.h>
#include<string.h>
#include<time.h>
#include<stdlib.h>

int state = 0x42;

struct Flag
{
	long int aa;
	long int ab;
	long int ac;
	long int ad;
	long int ae;
	long int af;
	long int ag;
	long int ah;
	long int ai;
	long int aj;
	long int ak;
	long int al;
	long int am;
	long int an;
	long int ao;
	long int ap;
	long int aq;
	long int ar;
	long int as;
	long int at;
	long int au;
	long int av;
	long int aw;
	long int ax;
	long int ay;
	long int az;
	long int ba;
	long int bb;
	long int bc;
	long int bd;
	long int be;
	long int bf;
	long int bg;
	long int bh;
	long int bi;
	long int bj;
	long int bk;
	long int bl;
	long int bm;
	long int bn;
	long int bo;
	long int bp;
	long int bq;
	long int br;
	long int bs;
	long int bt;
	long int bu;
	long int bv;
	long int bw;
	long int bx;
	long int by;
	long int bz;
	long int ca;
	long int cb;
	long int cc;
	long int cd;
	long int ce;
	long int cf;
	long int cg;
	long int ch;
	long int ci;
	long int cj;
	long int ck;
	long int cl;
	long int cm;
	long int cn;
	long int co;
	long int cp;
	long int cq;
	long int cr;
	long int cs;
	long int ct;
	long int cu;
	long int cv;
	long int cw;
	long int cx;
	long int cy;
	long int cz;
} flag;

// c + 19 % 256
char fanpiuneyuasbqee(char c, int r1, int r2)
{
	return (c + r1) % 256; 
}

char fnmsgndhtxwaaikn(char c, int r1, int r2)
{
	return fanpiuneyuasbqee(c, r1 - r2, r2); 
}

char fnbnlvpsknmvqnfs(char c, int r1, int r2)
{
	return fnmsgndhtxwaaikn(c, r1 / 198, r2); 
}

char fsijhayvuvoeekry(char c, int r1, int r2)
{
	return fnbnlvpsknmvqnfs(c, r1 - 81180, r2); 
}

char fzqfnuiqaklyixyd(char c, int r1, int r2)
{
	return fsijhayvuvoeekry(c, r1 * 198, r2); 
}

char frthcatplziuycxi(char c, int r1, int r2)
{
	return fzqfnuiqaklyixyd(c, r1 + 429, r2);
}

// state - 55 % 256
char fixheogisardtpxb(int c, int r1, int r2)
{
	return (c + r1) % 256; 
}

char fqvmtvyrwbtgrvml(int c, int r1, int r2)
{
	return fixheogisardtpxb(c, r1 - 2 * r2, r2);
}

char fmnltlwetqzjrbyy(int c, int r1, int r2)
{
	return fqvmtvyrwbtgrvml(c, r1 / (39 * r2 + 29), r2);
}

char fdvwhahiogiaskqy(int c, int r1, int r2)
{
	return fmnltlwetqzjrbyy(c, r1 - 2087 * r2, r2);
}

char fwwgvsshasezsads(int c, int r1, int r2)
{
	return fdvwhahiogiaskqy(c, r1 - 1595, r2);
}

char fcfnqmveklcrqfsm(int c, int r1, int r2)
{
	return fwwgvsshasezsads(c, r1 * 78, r2);
}

char fjdndjcbzriaukmh(int c, int r1, int r2)
{
	return fcfnqmveklcrqfsm(c, r1 * r1, r2);
}

char cast_magic(char c)
{
	int r = rand() % 256;
	
	c = frthcatplziuycxi(c, r, r) ^ fjdndjcbzriaukmh(state, r, r);
	state = state * 0x3;
	return c;
}

void init()
{
	flag.aa = 0x45b737817b841bdb;
    flag.ab = 0x267e07a86fc14218;
    flag.ac = 0x69e1b652cb729ea3;
    flag.ad = 0x5e7e7d051d86de97;
    flag.ae = 0xedbf6865511a9855;
    flag.af = 0xe9adc7ce415a746c;
    flag.ag = 0xdc7bed5d6251f988;
    flag.ah = 0xfed5090ff8dd37f2;
    flag.ai = 0xb71e68f9da8346ad;
    flag.aj = 0x8780488c7f496863;
    flag.ak = 0xc06fd17d9b01fbeb;
    flag.al = 0xf913113ddbdee8d9;
    flag.am = 0x4df758090ab8ae99;
    flag.an = 0x8dbcb4829778b4ac;
    flag.ao = 0xd569f78a9c092d0a;
    flag.ap = 0xf818ce39c8c4e7e8;
    flag.aq = 0xb5f78ecc2dbd59af;
    flag.ar = 0xb692b6805349836c;
    flag.as = 0xfd841f43943fda1f;
    flag.at = 0xeec1a93441962414;
    flag.au = 0x3a6225f7f4309551;
    flag.av = 0xed64258219350acc;
    flag.aw = 0x9e7041bf829e9218;
    flag.ax = 0x0e852a8a5bf2a625;
    flag.ay = 0xbf2c1037adb6935a;
    flag.az = 0x845bc1184914b2c5;
    flag.ba = 0x78a2716baae70af0;
    flag.bb = 0xecfc891acf2abc6b;
    flag.bc = 0xff85d0e086956650;
    flag.bd = 0x3bd5ccc8e5c2cfca;
    flag.be = 0x08e3445fb88f2ea7;
    flag.bf = 0x6eb31827288dc75c;
    flag.bg = 0xbd949fe065fd72dc;
    flag.bh = 0x72cffd6b0479d1e7;
    flag.bi = 0xa438d5c03f2eb3ca;
    flag.bj = 0x59d64e97c94aa915;
    flag.bk = 0xa1a2985307dda179;
    flag.bl = 0x1c9fc505b3ccd51a;
    flag.bm = 0xcfd54eec85426136;
    flag.bn = 0x7b874cdb59b2a3f2;
    flag.bo = 0x234e33c24416629e;
    flag.bp = 0x9d6dfc40278f87de;
    flag.bq = 0x7341628cebf7f575;
    flag.br = 0xa11946f5ef9cc128;
    flag.bs = 0xd65dba4a3574b26b;
    flag.bt = 0x16b1cc713ad76f02;
    flag.bu = 0xeed9cf98baa793db;
    flag.bv = 0x6eaf74fbaa9af375;
    flag.bw = 0xb2610aa0762ed640;
    flag.bx = 0x6b4f6183de5d240c;
    flag.by = 0xa48394a549c62a2e;
    flag.bz = 0x241b0f79668a8142;
    flag.ca = 0xe1b0578321943c9d;
    flag.cb = 0x782f86fe86458256;
    flag.cc = 0xaf2348c6b9f69dd6;
    flag.cd = 0x5f54cde00efa1f9a;
    flag.ce = 0x2139699f269a2a63;
    flag.cf = 0xbc6401dd6c230650;
    flag.cg = 0x535c467ced4548b4;
    flag.ch = 0x992b4d854d4422ed;
    flag.ci = 0xe130c4a4842a45ba;
    flag.cj = 0x2d66bf3290d89dab;
    flag.ck = 0x53aafbabb6fa49f4;
    flag.cl = 0x86e9e26843df6915;
    flag.cm = 0x1650dc001f8ce434;
    flag.cn = 0x6d646291142ce6b9;
    flag.co = 0x7b4213b860591b36;
    flag.cp = 0xaf3fe0568d293809;
    flag.cq = 0xfe2d60af51f5580a;
    flag.cr = 0x81f160dbf9b6a619;
    flag.cs = 0xcd9cc1d889f27660;
    flag.ct = 0xe9753ebc8996fde3;
    flag.cu = 0x091f91929bb90cac;
    flag.cv = 0x59f83c7ae10eb7b2;
    flag.cw = 0x51a745f693a2f9af;
    flag.cx = 0xc8dbb42bd8864676;
    flag.cy = 0x519a803ebd619bac;
    flag.cz = 0x5eda784f49a4d969;
}

int main()
{
	char inp[0x100];
	char* flag_ptr = (char*) &flag;
	init();
	srand(time(NULL));
	
	fputs("Welcome to the Magical Mystery Club.\nEnter your spell so we can see how worthy you are! If you succeed, the spell can also be used for other things...\n> ", stdout);
	scanf("%s", inp);
	for(int i = 0; i < strlen(inp); i++)
	{
		inp[i] = cast_magic(inp[i]);
	}
	if(memcmp(inp, flag_ptr + 52, 0x62) == 0)
	{
		fputs("You belong here, welcome!\n", stdout);
	} else {
		fputs("Your spell is not powerful enough...\n", stdout);
	}
	return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ARR_SIZE 2048

char ins[ARR_SIZE];
int ip, mp, brack, ip_end;

void jmp2closing() {
    int balance = 1;
	do
	{	
		ip++;
		if (ins[ip] == '[') balance++;
		else if(ins[ip] == ']') balance--;
		
	} while (balance != 0);
}

void jmp2opening() {
    int balance = 1;
	do
	{	
		ip--;
		if (ins[ip] == '[') balance--;
		else if(ins[ip] == ']') balance++;
		
	} while (balance != 0);
}

void proc_inp() {
    char ch;
    printf("Code : ");
    while ((ch=getchar())!='\n' && ch!=EOF && ip_end<ARR_SIZE)
    {
        switch (ch)
        {
        case '<': case '>': case '+': case '-': case ',': case '.': 
            ins[ip_end] = ch;
            ip_end++;
            break;
        case '[': 
            ins[ip_end] = ch;
            ip_end++;
            brack++;
            break;
        case ']':
            ins[ip_end] = ch;
            ip_end++;
            brack--;
            break;
        }
    }
}

void init_var() {
    ip = mp = brack = ip_end = 0;
    memset(ins, 0, ARR_SIZE*sizeof(char));
}

void interpret() {
    init_var();

    char mem[ARR_SIZE];
    void *addr = mem;
    memset(addr, 0, ARR_SIZE*sizeof(char));

    proc_inp();
    if (brack != 0) {
        printf("Unbalanced brackets. \n");
        return;
    }
    printf("\nOutput: ");

    while (ip != ip_end)
    {
        switch (ins[ip])
        {
        case '+':
			mem[mp]++;
			ip++;
			break;
		case '-':
			mem[mp]--;
			ip++;
			break;
		case '>':
            mp++;
			ip++;
			break;
		case '<':
			mp--;
			ip++;
			break;
		case '.':
			putchar(mem[mp]);
			ip++;
			break;
		case ',':
			mem[mp] = getchar();
			ip++;
			break;
		case '[':
			if (!mem[mp]) jmp2closing();
			ip++;
			break;
		case ']':
            if (mem[mp]) jmp2opening();
			ip++;
			break;
		case '\0':
			ip++;
			break;
        }
    }
}

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
}

int main() {
    init();

    while (1)
    {
        printf("\nBrainFuck C Interactive Interpreter. Max 2048 char instructions.\n1. Interpret code\n2. Exit\nInput : ");

        char inp = getchar();
        getchar();
        
        if (inp == '1') interpret();
        else if (inp == '2') break;   
    }
    return 0;
}
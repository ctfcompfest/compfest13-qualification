
/*
 * Cara compile : gcc -s -static -fno-stack-protector -no-pie -o anti_blind anti_blind.c
 *
 * NOTE : anti_blind dicompile dengan gcc versi 8.3.0 di OS debian (WSL)
 *
 * */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/ptrace.h>

void WIN(){
	system("cat flag.txt");
}

int vuln(){
	int manual_stack_protector = 0xcafebabe;
	char password[40];
	printf("[*] Masukkan password : ");
	// Menggunakan read() dibangin gets() agar null byte bisa diterima
	read(0, password, 70);
	if (manual_stack_protector != 0xcafebabe){
		// Exit ini bisa dipake untuk menganalisis binary-nya walaupun ada anti-debugger (ptrace traceme)
		exit(EXIT_FAILURE);
	}
	printf("[*] Bye!\n");
	return 0;
}

int main(int argc, char const *argv[]){

	setvbuf(stdout, 0, 2, 0);

	printf("[ INFO ] Pergi ke %p supaya dapet flag\n\n", WIN);

	if(ptrace(PTRACE_TRACEME, 0, 0, 0) < 0){
		printf("[-] Oops, kayaknya ada debugger\n");
		exit(EXIT_FAILURE);
	}

	while(1){
		vuln();
	}
	return 0;
}

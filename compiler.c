#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(){
	printf("Compiling...\n");
	system("gcc main.c -o main");
	system("clear");
	system("./main");
	return 0;
}

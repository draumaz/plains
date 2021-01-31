#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

//DEFINE NAVIGATION VARIABLES//	

char opt1[50];
char nav1[50];

//CLEAR MEMORY//

memset(opt1, '\0', 1000);
memset(nav1, '\0', 1000);

MAINMENU:

	//DEBUGGER START//
	//printf("\n");
	//printf("DEBUGGER\n");
	//printf("OPT1 = %s\n", opt1);
	//printf("NAV1 = %s\n", nav1);
	//printf("\n");
	//printf("\n");
	//DEBUGGER END//
	
	printf("\n");
	printf("==ADVENTURE GAME==\n");
	printf("==MADE BY DRAUMAZ IN 2021==\n");
	printf("==LOVINGLY CODED IN C==\n");
	printf("\n");

	printf("You awaken suddenly, finding yourself in the middle of a large,\ngrassy field. There doesn't seem to be a single sign of civilization.\n");
	printf("\n");
	printf("ACTION: \n");
	printf("\n");
	printf("LOOK AROUND [1] \n");
	printf("SIT DOWN [2] \n");
	printf("WIP [3] \n");
	printf("QUIT [Q] \n");
	printf("\n");
	printf("ACTION >> ");
	scanf("%s", opt1);

		//BEGIN SUB-MENU ONE//

SUB1:

	if(strcmp(opt1, "1")==0){
		printf("\n");
		printf("Peering just over the horizon, you can\njust barely make out the sight of a\nlarge hill.\n");
		printf("\n");
		printf("HEAD TOWARDS [1] \n");
		printf("STAND STILL [2] \n");
		printf("CHECK THE SKY [3] \n");
		printf("[B]ACK \n");
		printf("\n");
		printf("ACTION  >> ");
		scanf("%s", nav1);
	
		if(strcmp(nav1, "1")==0){
			memset(nav1, '\0', 1000);
			printf("\n");
			printf("Deciding to take a walk, you make your\nway towards the hill before realizing\nthat it is not a hill, but\nan evil creature!\n");
			printf("\n");
			printf("DI[E]\n");
			printf("[B]ACK\n");
			printf("\n");
			printf("ACTION >> ");
			scanf("%s", nav1);
			if(strcmp(nav1, "E")==0){
			printf("In a moment of mind-blowing wit, you\nwillingly let yourself die.\nNice going, genius.\n");
			printf("\n");
			printf("GAME OVER\n");
			printf("\n");
			return 0;
			}
			else {
			printf("You decide to head back to where you started.\nProbably for the best.\n");
			goto SUB1;
		}}

		if(strcmp(nav1, "2")==0){
			memset(nav1, '\0', 1000);
			printf("\n");
			printf("You remain motionless. Seems like a waste of time, doesn't it?.\n");
			printf("\n");
			printf("[E]H...\n");
			printf("[B]ACK\n");
			printf("\n");
			printf("ACTION >> ");
			scanf("%s", nav1);
			if(strcmp(nav1, "E")==0){
			printf("You continue standing there, and you stand there\n until time stops progressing. You did it!\nYou became god! ");
			printf("\n");
			printf("GAME...OVER?\n");
			printf("\n");
			return 0;
			}
			else {
			goto SUB1;
		}}

		if(strcmp(nav1, "3")==0){
			memset(nav1, '\0', 1000);
			printf("\n");
			printf("You lay down on the grassy plains and get a good\nlook at the sky. It's beautiful - clouds gently pattern\n the bright blue sky.\n");
			printf("\n");
			printf("[E]XAMINE\n");
			printf("[B]ACK\n");
			printf("\n");
			printf("ACTION >> ");
			scanf("%s", nav1);
			if(strcmp(nav1, "E")==0){
			printf("Upon closer inspection...that's not the sky at all!\nIt seems you're on a distant planet.\n");
			printf("\n");
			printf("ACHIEVEMENT UNLOCKED: AWARENESS\n");
			return 0;
			}
			else {
			goto SUB1;
		}}

		if(strcmp(nav1, "B")==0){
			printf("You briefly consider checking it out...\nbut it's probably best to stick around here,\nat least for now.\n");
			goto MAINMENU;
		}}
		
		//END SUB-MENU ONE//

		//BEGIN SUB-MENU TWO//

SUB2:
//SIT DOWN//

	if(strcmp(opt1, "2")==0){
		memset(nav1, '\0', 1000);
		printf("You sit down on the warm grass. You feel the sun shining...\nBut why exactly are you here?\n");
		printf("REMEMBER [1] \n");
		printf("S2O[2] \n");
		printf("S2O[3] \n");
		printf("[B]ACK \n");
		printf("Please choose a submenu >> ");
		scanf("%s", nav1);
		
		if(strcmp(nav1, "1")==0){
			memset(nav1, '\0', 1000);
			printf("You start to remember how you got here...\n.\n");
			printf("THINK HARD[E]R\n");
			printf("[B]ACK\n");
			printf("\n");
			printf("ACTION >> ");
			scanf("%s", nav1);
			
			//TODO CONSTRUCT CONCEPT//

			if(strcmp(nav1, "E")==0){
			printf("LOREM IPSUM");
			goto MAINMENU;
			}
			else {
			goto SUB2;
		}}

		if(strcmp(nav1, "2")==0){
			memset(nav1, '\0', 1000);
			printf("You have entered S2O2.\n");
			printf("[E]XIT\n");
			printf("[B]ACK\n");
			printf("Please make a choice >> ");
			scanf("%s", nav1);
			if(strcmp(nav1, "E")==0){
			printf("Exiting... ");
			goto MAINMENU;
			}
			else {
			goto SUB2;
		}}

		if(strcmp(nav1, "3")==0){
			memset(nav1, '\0', 1000);
			printf("You have entered S2O3.\n");
			printf("[E]XIT\n");
			printf("[B]ACK\n");
			printf("Please make a choice >> ");
			scanf("%s", nav1);
			if(strcmp(nav1, "E")==0){
			printf("Exiting... ");
			goto MAINMENU;
			}
			else {
			goto SUB2;
		}}

		if(strcmp(nav1, "B")==0){
			goto MAINMENU;
		}}
	
		//END SUB-MENU TWO//
	
		//BEGIN SUB-MENU THREE//

SUB3:
//WIP//

	if(strcmp(opt1, "3")==0){
		memset(nav1, '\0', 1000);
		printf("Welcome to the third Submenu.\n");
		printf("S3O[1] \n");
		printf("S3O[2] \n");
		printf("S3O[3] \n");
		printf("[B]ACK \n");
		printf("Please choose a submenu >> ");
		scanf("%s", nav1);

		if(strcmp(nav1, "1")==0){
			memset(nav1, '\0', 1000);
			printf("You have entered S3O1.\n");
			printf("[E]XIT\n");
			printf("[B]ACK\n");
			printf("Please make a choice >> ");
			scanf("%s", nav1);
			if(strcmp(nav1, "E")==0){
			printf("Exiting... ");
			goto MAINMENU;
			}
			else {
			goto SUB3;
		}}

		if(strcmp(nav1, "2")==0){
			memset(nav1, '\0', 1000);
			printf("You have entered S3O2.\n");
			printf("[E]XIT\n");
			printf("[B]ACK\n");
			printf("Please make a choice >> ");
			scanf("%s", nav1);
			if(strcmp(nav1, "E")==0){
			printf("Exiting... ");
			goto MAINMENU;
			}
			else {
			goto SUB3;
		}}

		if(strcmp(nav1, "3")==0){
			memset(nav1, '\0', 1000);
			printf("You have entered S3O3.\n");
			printf("[E]XIT\n");
			printf("[B]ACK\n");
			printf("Please make a choice >> ");
			scanf("%s", nav1);
			if(strcmp(nav1, "E")==0){
			printf("Exiting... ");
			goto MAINMENU;
			}
			else {
			goto SUB3;
		}}
		if(strcmp(nav1, "B")==0){
			goto MAINMENU;
		}}

		//END SUB-MENU THREE//
	if(strcmp(opt1, "Q")==0){
		printf("Exiting... \n");
		return 0;
	}

	return 0;
}

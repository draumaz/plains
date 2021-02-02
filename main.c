#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {

//DEFINE NAVIGATION VARIABLES//	

char opt1[50];
char nav1[50];

//CLEAR MEMORY//

memset(opt1, '\0', 50);
memset(nav1, '\0', 50);

	system("clear");

	//DEBUGGER START//
	//printf("\n");
	//printf("DEBUGGER\n");
	//printf("OPT1 = %s\n", opt1);
	//printf("NAV1 = %s\n", nav1);
	//printf("\n");
	//printf("\n");
	//DEBUGGER END//
	
	printf("\n==THE PLAINS==\n");
	printf("==MADE BY DRAUMAZ IN 2021==\n");
	printf("==LOVINGLY CODED IN C==\n");
	printf("\n");
	sleep(1);
	goto MAINMENU;

MAINMENU:

	system("clear");
	printf("\nThe Plains v0.02\n\n");
	printf("You awaken suddenly, finding yourself in the middle of a large,\ngrassy field. There doesn't seem to be a single sign of civilization.\nThe only thing that really sticks out to you, is a massive\nhill just a couple hundred meters away from you.\n");
	printf("\n\n");
	printf("CHECK THE HILL OUT [1] \n");
	printf("LOOK AROUND [2] \n");
	printf("WIP [3] [NON-FUNCTIONAL] \n");
	printf("QUIT [Q] \n");
	printf("\n");
	printf("ACTION >> ");
	scanf("%s", opt1);

		//BEGIN SUB-MENU ONE//

SUB1:

	if(strcmp(opt1, "1")==0){
		system("clear");
		printf("\nThe Plains v0.02\n\n");
		printf("Peering just over the horizon, you can just barely make out\nthe sight of a large hill.\n");
		printf("\n");
		printf("HEAD TOWARDS [1] \n");
		printf("STAND STILL [2] \n");
		printf("CHECK THE SKY [3] \n");
		printf("[B]ACK \n");
		printf("\n");
		printf("ACTION  >> ");
		scanf("%s", nav1);
	
		if(strcmp(nav1, "1")==0){
			system("clear");
			printf("\nThe Plains v0.02\n\n");
			memset(nav1, '\0', 50);
			printf("Deciding to take a walk, you make your\nway towards the hill before realizing\nthat it is not a hill, but\nan evil creature!\n");
			printf("\n");
			printf("DI[E]\n");
			printf("[B]ACK\n");
			printf("\n");
			printf("ACTION >> ");
			scanf("%s", nav1);
			if(strcmp(nav1, "E")==0){
			printf("\nIn a moment of mind-blowing wit, you\nwillingly let yourself die.\nNice going, genius.\n");
			printf("\n");
			printf("GAME OVER\n");
			printf("\n");
			sleep(1);
			return 0;
			}
			else {
			printf("\nYou decide to head back to where you started.\nProbably for the best.\n");
			goto SUB1;
		}}

		if(strcmp(nav1, "2")==0){
			system("clear");
			printf("\nThe Plains v0.02\n\n");
			memset(nav1, '\0', 50);
			printf("You remain motionless. Seems like a waste of time, doesn't it?.\n");
			printf("\n");
			printf("[E]H...\n");
			printf("[B]ACK\n");
			printf("\n");
			printf("ACTION >> ");
			scanf("%s", nav1);
			if(strcmp(nav1, "E")==0){
			printf("\nYou continue standing there, and you stand there until time stops progressing.\nYou did it! You became god!\n");
			printf("\n");
			printf("GAME...OVER?\n");
			printf("\n");
			sleep(1);
			return 0;
			}
			else {
			goto SUB1;
		}}

		if(strcmp(nav1, "3")==0){
			system("clear");
			printf("\nThe Plains v0.02\n\n");
			memset(nav1, '\0', 50);
			printf("You lay down on the grassy plains and get a good\nlook at the sky. It's beautiful - clouds gently pattern\nthe bright blue sky.\n");
			printf("\n");
			printf("[E]XAMINE\n");
			printf("[B]ACK\n");
			printf("\n");
			printf("ACTION >> ");
			scanf("%s", nav1);
			if(strcmp(nav1, "E")==0){
			printf("\nUpon closer inspection...that's not the sky at all!\nIt seems you're on a distant planet.\n");
			printf("\n");
			printf("ACHIEVEMENT UNLOCKED: AWARENESS\n");
			sleep(4);
			goto SUB1;
			}
			else {
			goto SUB1;
		}}

		if(strcmp(nav1, "B")==0){
			memset(nav1, '\0', 50);
			printf("\nThe Plains v0.02\n\n");
			printf("You briefly consider checking it out...\nbut it's probably best to stick around here,\nat least for now.\n");
			goto MAINMENU;
		}}
		
		//END SUB-MENU ONE//

		//BEGIN SUB-MENU TWO//

SUB2:
//SIT DOWN//

	if(strcmp(opt1, "2")==0){
		system("clear");
		memset(nav1, '\0', 50);
		printf("\nThe Plains v0.02\n\n");
		printf("You sit down on the warm grass. You feel the sun shining...\nBut why exactly are you here?\n\n\n");
		printf("REMEMBER [1] \n");
		printf("DISREGARD [2] \n");
		printf("INTROSPECT [3] \n");
		printf("[B]ACK \n");
		printf("\nACTION >> ");
		scanf("%s", nav1);
		
		if(strcmp(nav1, "1")==0){
			system("clear");
			memset(nav1, '\0', 50);
			printf("\nThe Plains v0.02\n\n");
			printf("You start to remember how you got here...\n\n");
			printf("THINK HARD[E]R\n");
			printf("[B]ACK\n");
			printf("\n");
			printf("ACTION >> ");
			scanf("%s", nav1);
			if(strcmp(nav1, "E")==0){
			printf("\n");
			printf("Suddenly, it all comes flooding back...\nYou look down at your hands, and realize that\nyou have been in an astral projection for the last hour or so.\nYou come to your senses and wake up on your bed.\n\n");
			printf("TRUE ENDING UNLOCKED!\n\n");
			printf("==THE END==\n\n");
			return 0;
			}
			else {
			goto SUB2;
		}}

		if(strcmp(nav1, "2")==0){
			system("clear");
			memset(nav1, '\0', 50);
			printf("\nThe Plains v0.02\n\n");
			printf("You're right, it's probably not a big deal.\nNot like you're in the middle of nowhere, or anything.\n");
			printf("ACTUALL-[E]...\n");
			printf("[B]ACK\n");
			printf("ACTION >> ");
			scanf("%s", nav1);
			if(strcmp(nav1, "E")==0){
			printf("\n");
			printf("Your flagrant disregard becomes so immense\nthat you end up at the beginning of your adventure.\n");
			goto MAINMENU;
			}
			else {
			goto SUB2;
		}}

		if(strcmp(nav1, "3")==0){
			system("clear");
			memset(nav1, '\0', 50);
			printf("\nThe Plains v0.02\n\n");
			printf("With introspection of your soul, the truth may be\ncloser to reveal than ever.\n");
			printf("DIG DE[E]PER\n");
			printf("[B]ACK\n");
			printf("ACTION >> ");
			scanf("%s", nav1);
			if(strcmp(nav1, "E")==0){
			printf("\n");
			printf("Your wish came true!\n");
			printf("GAME OVER!\n");
			return 0;
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
//TODO THIS SECTION//

	if(strcmp(opt1, "3")==0){
		system("clear");
		memset(nav1, '\0', 50);
		printf("Welcome to the third Submenu.\n");
		printf("S3O[1] \n");
		printf("S3O[2] \n");
		printf("S3O[3] \n");
		printf("[B]ACK \n");
		printf("Please choose a submenu >> ");
		scanf("%s", nav1);

		if(strcmp(nav1, "1")==0){
			system("clear");
			memset(nav1, '\0', 50);
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
			system("clear");
			memset(nav1, '\0', 50);
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
			system("clear");
			memset(nav1, '\0', 50);
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
		system("clear");
		return 0;
		}	
		else {
		printf("Did you mean something else?\n");
		memset(nav1, '\0', 50);
		memset(opt1, '\0', 50);
		goto MAINMENU;
	}
}

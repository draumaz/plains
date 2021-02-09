#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {

//DEFINE//	

char opt1[50]; //MENU//
char nav1[50]; //TREES & SUBTREES//
int var1; //TOOL FLAG//
int var2; //PLAYED FLAG//
int var3; //T-E FLAG//
int var4; //DEBUG FLAG//

//INIT//

system("clear");
var1 = 0;
var2 = 0;
var3 = 0;
var4 = 0;

//SPLASH//

printf("\n==THE PLAINS==\n");
printf("==MADE BY DRAUMAZ IN 2021==\n");
printf("==LOVINGLY CODED IN C==\n");
printf("==CHARACTER DESIGN AND INSPIRATION BY BRYCE CANO==\n\n");
sleep(2);

//BEGIN MAIN//

MAINMENU:
	system("clear");
	memset(opt1, '\0', 50);
	memset(nav1, '\0', 50);
	printf("\nThe Plains v0.11\n\n");
	if(var4 == 1){
	printf("OPT1 = %s, NAV1 = %s, VAR1 = %d\nVAR2 = %d, VAR3 = %d, VAR4 = %d\n\n", opt1, nav1, var1, var2, var3, var4);
	}
	printf("You are Liam, an astronaut who found himself crash-landed in an unknown place.\n");
	printf("You awaken suddenly, finding yourself in the middle of a large, grassy field.\nYou can see some hills, a mountain range, and strange flora.\n\n");
	printf("CHECK THE HILL OUT [1] \n");
	printf("LOOK AROUND [2] \n");
	printf("USE YOUR TOOLS [3] \n");
	if(var3 == 1){
	printf("... [4] \n");
	}
	printf("QUIT [Q] \n\n");
	printf("ACTION >> ");
	scanf("%s", opt1);

//BEGIN EXIT HANDLER//

	if(strcmp(opt1, "Q")==0){
	if(var2 == 1){
	system("clear");
	printf("\n==THANK YOU==\n==FOR PLAYING!==\n");
	sleep(1);
	return 0;
	}
	if(var2 == 0){
	system("clear");
	printf("\nYou quit immediately?\nOh well.\n\n");
	sleep(2);
	return 0;
	}}
	if(strcmp(opt1, "q")==0){
	if(var2 == 1){
	system("clear");
	printf("\n==THANK YOU==\n==FOR PLAYING!==\n");
	sleep(1);
	return 0;
	}
	if(var2 == 0){
	system("clear");
	printf("\nYou quit immediately?\nOh well.\n\n");
	sleep(2);
	return 0;
	}}

//END EXIT HANDLER//
//
//BEGIN DEBUGGER//

	if(strcmp(opt1, "liam")==0){
	var2 = 1;
	var4 = 1;
	printf("\nDeveloper mode activated\n");
	sleep(1);
	goto MAINMENU;
	}
	if(strcmp(opt1, "stahp")==0){
	var2 = 1;
	var4 = 0;
	printf("\nDeveloper mode deactivated\n");
	sleep(1);
	goto MAINMENU;
	}

//END DEBUGGER//
//
//BEGIN TREE 1//

SUB1:
	if(strcmp(opt1, "1")==0){
	system("clear");
	var2 = 1;
	printf("\nThe Plains v0.11\n\n");
	if(var4 == 1){
	printf("OPT1 = %s, NAV1 = %s, VAR1 = %d\nVAR2 = %d, VAR3 = %d, VAR4 = %d\n\n", opt1, nav1, var1, var2, var3, var4);
	}
	printf("Peering over the horizon, you can just barely make out\nthe sight of a large hill.\n\n");
	printf("HEAD TOWARDS [1] \n");
	printf("STAND STILL [2] \n");
	printf("CHECK THE SKY [3] \n");
	printf("[B]ACK \n");
	printf("\n\nACTION >> ");
	memset(nav1, '\0', 50);
	scanf("%s", nav1);

		if(strcmp(nav1, "1")==0){
		system("clear");
		printf("\nThe Plains v0.11\n\n");
		if(var4 == 1){
		printf("OPT1 = %s, NAV1 = %s, VAR1 = %d\nVAR2 = %d, VAR3 = %d, VAR4 = %d\n\n", opt1, nav1, var1, var2, var3, var4);
		}
		memset(nav1, '\0', 50);
		printf("Deciding to take a walk, you make your way towards the hill\nbefore realizing that it is not a hill, but an evil creature!\n\n");
		printf("DI[E]\n");
		printf("[B]ACK\n\n");
		printf("\n\n\nACTION >> ");
		scanf("%s", nav1);
			if(strcmp(nav1, "E")==0){
			printf("\nIn a moment of mind-blowing wit, you willingly let yourself die.\nNice going, genius.\n\n");
			printf("GAME OVER\n\n");
			sleep(5);
			return 0;
			}
	
			if(strcmp(nav1, "e")==0){
			printf("\nIn a moment of mind-blowing wit, you willingly let yourself die.\nNice going, genius.\n\n");
			printf("GAME OVER\n\n");
			sleep(5);
			return 0;
			}
			if(strcmp(nav1, "B")==0){
			printf("\nYou decide to head back to where you started.\nProbably for the best.\n");
			sleep(2);
			goto SUB1;
			}
			if(strcmp(nav1, "b")==0){
			printf("\nYou decide to head back to where you started.\nProbably for the best.\n");
			sleep(2);
			goto SUB1;
			}
	
			else {
			printf("\nDid you mean something else?\n");
			sleep(1);
			goto SUB1;
			}
		}

		if(strcmp(nav1, "2")==0){
		system("clear");
		printf("\nThe Plains v0.11\n\n");
		if(var4 == 1){
		printf("OPT1 = %s, NAV1 = %s, VAR1 = %d\nVAR2 = %d, VAR3 = %d, VAR4 = %d\n\n", opt1, nav1, var1, var2, var3, var4);
		}
		memset(nav1, '\0', 50);
		printf("You remain motionless. Seems like a waste of time, doesn't it?.\n\n");
		printf("[E]H...\n");
		printf("[B]ACK\n");
		printf("\n\n\n\n\nACTION >> ");
		scanf("%s", nav1);
			if(strcmp(nav1, "B")==0){
			printf("\nYou stop being motionless and return to a life full of motion.\n");
			sleep(2);
			goto SUB1;
			}
			if(strcmp(nav1, "b")==0){
			printf("\nYou stop being motionless and return to a life full of motion.\n");
			sleep(2);
			goto SUB1;
			}
			if(strcmp(nav1, "E")==0){
			printf("\nYou continue standing there.\n\n");
			sleep(10);
			printf("\nK[E]EP STANDING");
			printf("\n[B]ACK\n");
			printf("\nACTION >> ");
			memset(nav1, '\0', 50);
			scanf("%s", nav1);
				if(strcmp(nav1, "E")==0){
				var3 = 1;
				sleep(5);
				printf("\nStanding there completely motionless, it gives you the feeling that everything's going to be alright.\n");
				sleep(4);
				goto SUB1;
				}
				if(strcmp(nav1, "e")==0){
				sleep(5);
				var3 = 1;
				printf("\nStanding there completely motionless, it gives you the feeling that eberything's going to be alright.\n");
				sleep(4);
				goto SUB1;
				}
				if(strcmp(nav1, "B")==0){
				printf("\nYou stop being motionless and return to a life full of motion.\n");
				sleep(2);
				goto SUB1;
				}
				if(strcmp(nav1, "b")==0){
				printf("\nYou stop being motionless and return to a life full of motion.\n");
				sleep(2);
				goto SUB1;
				}
				else {
				printf("\nDid you mean something else?\n");
				sleep(1);
				goto SUB1;
				}}

			if(strcmp(nav1, "e")==0){
			printf("\nYou continue standing there.\n\n");
			sleep(10);
			printf("\nK[E]EP STANDING");
			printf("\n[B]ACK\n");
			printf("\nACTION >> ");
			memset(nav1, '\0', 50);
			scanf("%s", nav1);
				if(strcmp(nav1, "E")==0){
				sleep(5);
				var3 = 1;
				printf("\nStanding there completely motionless, it gives you the feeling that everything's going to be alright.\n");
				sleep(4);
				goto SUB1;
				}
				if(strcmp(nav1, "e")==0){
				sleep(5);
				var3 = 1;
				printf("\nStanding there completely motionless, it gives you the feeling that everything's going to be alright.\n");
				sleep(4);
				goto SUB1;
				}
				if(strcmp(nav1, "B")==0){
				printf("\nYou stop being motionless and return to a life full of motion.\n");
				sleep(2);
				goto SUB1;
				}
				if(strcmp(nav1, "b")==0){
				printf("\nYou stop being motionless and return to a life full of motion.\n");
				sleep(2);
				goto SUB1;
				}
				else{
				printf("\nDid you mean something else?\n");
				sleep(1);
				goto SUB1;
				}}	
			}
	
		if(strcmp(nav1, "3")==0){
		system("clear");
		printf("\nThe Plains v0.11\n\n");
		if(var4 == 1){
		printf("OPT1 = %s, NAV1 = %s, VAR1 = %d\nVAR2 = %d, VAR3 = %d, VAR4 = %d\n\n", opt1, nav1, var1, var2, var3, var4);
		}
		memset(nav1, '\0', 50);
		printf("You lay down on the grassy plains and get a good look at the sky.\nIt's beautiful - clouds gently pattern the great blue expanse.\n\n");
		printf("[E]XAMINE\n");
		printf("[B]ACK\n\n");
		printf("\n\n\nACTION >> ");
		scanf("%s", nav1);
			if(strcmp(nav1, "E")==0){
			printf("\nYou feel truly refreshed. Perhaps a crash landing was just what you needed.");
			printf("\n...shouldn't your team have checked in on you by now?\n");
			sleep(5);
			goto SUB1;
			}
			if(strcmp(nav1, "e")==0){
			printf("\nYou feel truly refreshed. Perhaps a crash landing was just what you needed.");
			printf("\n...shouldn't your team have checked in on you by now?\n");
			sleep(5);
			goto SUB1;
			}
			if(strcmp(nav1, "B")==0){
			printf("\nAs beautiful as the clouds are, you have things to do.\n");
			sleep(3);
			goto SUB1;
			}
			if(strcmp(nav1, "b")==0){
			printf("\nAs beautiful as the clouds are, you have things to do.\n");
			sleep(3);
			goto SUB1;
			}
			else {
			printf("\nDid you mean something else?\n");
			sleep(1);
			goto SUB1;
	}}

		if(strcmp(nav1, "B")==0){
		printf("\nYou consider checking the mountain out...\nYou've got better things to do.\n");
		sleep(2);
		goto MAINMENU;
	}
		if(strcmp(nav1, "b")==0){
		printf("\nYou consider checking the mountain out...\nYou've got better things to do.\n");
		sleep(2);
		goto MAINMENU;
		}

		else {
		printf("\nDid you mean something else?\n");
		sleep(1);
		goto SUB1;
		}
	}

//END TREE 1//
//
//BEGIN TREE 2//	

SUB2:
	if(strcmp(opt1, "2")==0){
	var2 = 1;
	system("clear");
	memset(nav1, '\0', 50);
	printf("\nThe Plains v0.11\n\n");
	if(var4 == 1){
	printf("OPT1 = %s, NAV1 = %s, VAR1 = %d\nVAR2 = %d, VAR3 = %d, VAR4 = %d\n\n", opt1, nav1, var1, var2, var3, var4);
	}
	printf("You sit down on the warm grass. You feel the sun shining...\nTimes like these are perfect to sit down and think.\n\n");
	printf("\nRECENT EVENTS [1]");
	printf("\nSURROUNDINGS [2]");
	printf("\nABOUT YOURSELF [3]");
	printf("\n[B]ACK \n\n");
	printf("ACTION >> ");
	scanf("%s", nav1);
	
		if(strcmp(nav1, "1")==0){
		system("clear");
		memset(nav1, '\0', 50);
		printf("\nThe Plains v0.11\n\n");
		if(var4 == 1){
		printf("OPT1 = %s, NAV1 = %s, VAR1 = %d, VAR2 = %d, VAR3 = %d, VAR4 = %d\n\n", opt1, nav1, var1, var2, var3, var4);
		}
		printf("You were on a mission to a different planet, and something happened...\nyou can't exactly remember.\n\n");
		printf("WHAT [E]LSE?\n");
		printf("[B]ACK\n\n");
		printf("\n\n\nACTION >> ");
		scanf("%s", nav1);
			if(strcmp(nav1, "E")==0){
			printf("\nBack at your home world, you are a successful astronaut, and spacetravel has been\nan interest of yours as long as you can remember.\n\n");
			sleep(5);
			printf("...you have a life to get back to. People that care about you.\n");
			sleep(4);
			goto SUB2;
			}
			if(strcmp(nav1, "e")==0){
			printf("\nBack at your home world, you are a successful astronaut, and spacetravel has been\nan interest of yours as long as you can remember.\n\n");
			sleep(5);
			printf("...you have a life to get back to. People that care about you.\n");
			sleep(4);
			goto SUB2;
			}
			if(strcmp(nav1, "B")==0){
			printf("\nIt's probably nothing to worry about.\n");
			sleep(2);
			goto SUB2;
			}
			if(strcmp(nav1, "b")==0){
			printf("\nIt's probably nothing to worry about.\n");
			sleep(2);
			goto SUB2;
			}
			else {
			printf("\nDid you mean something else?\n");
			sleep(1);
			goto SUB2;
			}
		}

		if(strcmp(nav1, "2")==0){
		system("clear");
		memset(nav1, '\0', 50);
		printf("\nThe Plains v0.11\n\n");
		if(var4 == 1){
		printf("OPT1 = %s, NAV1 = %s, VAR1 = %d\nVAR2 = %d, VAR3 = %d, VAR4 = %d\n\n", opt1, nav1, var1, var2, var3, var4);
		}
		printf("Seems like your ship has broken apart, pieces of it strewn around you.\n\n");
		printf("CH[E]CK YOUR SHIP\n");
		printf("[B]ACK\n\n");
		printf("\n\n\n\nACTION >> ");
		scanf("%s", nav1);
			if(strcmp(nav1, "E")==0){
			printf("\nLooks pretty destroyed. You can see some foodstuffs and items you brought,\nbut the machine is toast.\n");
			sleep(4);
			printf("You decide to go back to where you landed.\n");
			sleep(2);
			goto MAINMENU;
			}
			if(strcmp(nav1, "e")==0){
			printf("\nLooks pretty destroyed. You can see some foodstuffs and items you brought,\nbut the machine is toast.\n");
			sleep(4);
			printf("You decide to go back to where you landed.\n");
			sleep(2);
			goto MAINMENU;
			}
			if(strcmp(nav1, "B")==0){
			goto SUB2;
			}
			if(strcmp(nav1, "B")==0){
			goto SUB2;
			}
			else {
			printf("\nDid you mean something else?\n");
			sleep(1);
			goto SUB2;
			}
		}

		if(strcmp(nav1, "3")==0){
		system("clear");
		memset(nav1, '\0', 50);
		printf("\nThe Plains v0.11\n\n");
		if(var4 == 1){
		printf("OPT1 = %s, NAV1 = %s, VAR1 = %d\nVAR2 = %d, VAR3 = %d, VAR4 = %d\n\n", opt1, nav1, var1, var2, var3, var4);
		}
		printf("You're Liam!\n\n");
		printf("MOR[E]\n");
		printf("[B]ACK\n\n");
		printf("\n\n\n\nACTION >> ");
		scanf("%s", nav1);
			if(strcmp(nav1, "E")==0){
			printf("\nYou're of small stature and tan shade. Your spacesuit is intricate and comfortable... Especially against this grass.\n");
			sleep(4);
			goto SUB2;
			}
			if(strcmp(nav1, "e")==0){
			printf("\nYou're of small stature and tan shade. Your spacesuit is intricate and comfortable... Esepcially against this grass.\n");
			sleep(4);
			goto SUB2;
			}
			if(strcmp(nav1, "B")==0){
			printf("\nWith newfound knowledge of yourself, you decide to head back.\n");
			sleep(3);
			goto SUB2;
			}
			if(strcmp(nav1, "b")==0){
			printf("\nWith newfound knowledge of yourself, you decide to head back.\n");
			sleep(3);
			goto SUB2;
			}
			else {
			printf("\nDid you mean something else?\n");
			sleep(1);
			goto SUB2;
		}}
	
		if(strcmp(nav1, "B")==0){
		printf("\nSitting down on the grass is nice, but you've got work to do.\n");
		sleep(2);
		goto MAINMENU;
	}
		if(strcmp(nav1, "b")==0){
		printf("\nSitting down on the grass is nice, but you've got work to do.\n");
		sleep(2);
		goto MAINMENU;
		}

		else {
		printf("\nDid you mean something else?\n");
		sleep(1);
		goto SUB2;
		}
	}
	
//END TREE 2//
//		
//BEGIN TREE 3//

SUB3:
		if(strcmp(opt1, "3")==0){
		var2 = 1;
		system("clear");
		memset(nav1, '\0', 50);
		printf("\nThe Plains v0.11\n\n");
		if(var4 == 1){
		printf("OPT1 = %s, NAV1 = %s, VAR1 = %d\nVAR2 = %d, VAR3 = %d, VAR4 = %d\n\n", opt1, nav1, var1, var2, var3, var4);
		}
		printf("Stranded on this distant planet, you decide to use the tools at your disposal.\n\n");
		printf("PHONE [1] \n");
		printf("RADAR [2] \n");
		printf("SCANNER [3] \n");
		printf("[B]ACK \n\n");
		printf("\n\n\nACTION >> ");
		scanf("%s", nav1);
			if(strcmp(nav1, "1")==0){
			system("clear");
			memset(nav1, '\0', 50);
			var1 = 1;
			printf("\nThe Plains v0.11\n\n");
			if(var4 == 1){
			printf("OPT1 = %s, NAV1 = %s, VAR1 = %d\nVAR2 = %d, VAR3 = %d, VAR4 = %d\n\n", opt1, nav1, var1, var2, var3, var4);
			}
			printf("You pull out your phone. Unsurprisingly, the signal is rather weak.\n\n");
			printf("T[E]XT A FRIEND\n");
			printf("[B]ACK\n\n");
			printf("\n\n\n\nACTION >> ");
			scanf("%s", nav1);
			if(strcmp(nav1, "E")==0){
			printf("\nYou try texting a friend from work. Your phone just shuts off...\n");
			sleep(4);
			goto SUB3;
			}
			if(strcmp(nav1, "e")==0){
			printf("\nYou try texting a friend from work. Your phone just shuts off...\n");
			sleep(4);
			goto SUB3;
			}
			if(strcmp(nav1, "B")==0){
			printf("\nWhat good's a phone when there's no connection?\n");
			sleep(3);
			goto SUB3;
			}
			if(strcmp(nav1, "b")==0){
			printf("\nWhat good's a phone when there's no connection?\n");
			sleep(3);
			goto SUB3;
			}
			else {
			printf("\nDid you mean something else?\n");
			sleep(1);
			goto SUB3;
			}
		}

			if(strcmp(nav1, "2")==0){
			system("clear");
			var1 = 1;
			memset(nav1, '\0', 50);
			printf("\nThe Plains v0.11\n\n");
			if(var4 == 1){
			printf("OPT1 = %s, NAV1 = %s, VAR1 = %d\nVAR2 = %d, VAR3 = %d, VAR4 = %d\n\n", opt1, nav1, var1, var2, var3, var4);
			}
			printf("Using your radar, you try to establish contact.\n\n");
			printf("SCAN HARD[E]R\n");
			printf("[B]ACK\n\n");
			printf("\n\n\n\nACTION >> ");
			scanf("%s", nav1);
				if(strcmp(nav1, "E")==0){
				printf("\nPushing the radar to its limits, you can see a signal coming from your galaxy.\nUnfortunately, your phone can't send signals that far.\n");
				sleep(5);
				goto SUB3;
				}
				if(strcmp(nav1, "e")==0){
				printf("\nPushing the radar to its limits, you can see a signal coming from your galaxy.\nUnfortunately, your phone can't send signals that far.\n");
				sleep(5);
				goto SUB3;
				}
				if(strcmp(nav1, "B")==0){
				goto SUB3;
				}
				if(strcmp(nav1, "b")==0){
				goto SUB3;
				}
				else {
				printf("\nDid you mean something else?\n");
				sleep(1);
				goto SUB3;
				}
		}

			if(strcmp(nav1, "3")==0){
			system("clear");
			var1 = 1;
			memset(nav1, '\0', 50);
			printf("\nThe Plains v0.11\n\n");
			if(var4 == 1){
			printf("OPT1 = %s, NAV1 = %s, VAR1 = %d\nVAR2 = %d, VAR3 = %d, VAR4 = %d\n\n", opt1, nav1, var1, var2, var3, var4);
			}
			printf("You pull out your scanner. You have a couple options...\n\n");
			printf("[A]TMOSPHERE\n");
			printf("[L]OCATION\n");
			printf("[S]IGNAL\n");
			printf("[B]ACK\n\n");
			printf("\n\n\n\nACTION >> ");
			scanf("%s", nav1);
				if(strcmp(nav1, "A")==0){
				printf("\nThe atmosphere on this planet is shockingly similar to that of your own.\n");
				sleep(4);
				goto SUB3;
				}
				if(strcmp(nav1, "a")==0){
				printf("\nThe atmosphere on this planet is shockingly similar to that of your own.\n");
				sleep(4);
				goto SUB3;
				}
				if(strcmp(nav1, "L")==0){
				printf("\nTriangulating your location with the scanner, it seems you're a long ways from home.\n");
				sleep(4);
				goto SUB3;
				}
				if(strcmp(nav1, "l")==0){
				printf("\nTriangulating your location with the scanner, it seems you're a long ways from home.\n ");
				sleep(4);
				goto SUB3;
				}
				if(strcmp(nav1, "S")==0){
				printf("\nThe signal appears to be very weak, certainly not enough to reach anyone.\n");
				sleep(4);
				goto SUB3;
				}
				if(strcmp(nav1, "s")==0){
				printf("\nThe signal appears to be very weak, certainly not enough to reach anyone.\n");
				sleep(4);
				goto SUB3;
				}
				if(strcmp(nav1, "B")==0){
				goto SUB3;
				}
				if(strcmp(nav1, "b")==0){
				goto SUB3;
				}
				else {
				printf("\nDid you mean something else?\n");
				sleep(1);
				goto SUB3;
		}}

		if(strcmp(nav1, "B")==0){
		if(var1 == 1){
		printf("\nHaving used your tools, you head back to where you landed.\n");
		sleep(3);
		goto MAINMENU;
		}
		if(var1 == 0){
		printf("\nYou head back to where you landed.\n");
		sleep(2);
		goto MAINMENU;
		}}
		if(strcmp(nav1, "b")==0){
		if(var1 == 1){
		printf("\nHaving used your tools, you head back to where you landed.\n");
		sleep(3);
		goto MAINMENU;
		}
		if(var1 == 0){
		printf("\nYou head back to where you landed.\n");
		sleep(2);
		goto MAINMENU;
		}}
		else {
		printf("\nDid you mean something else?\n");
		sleep(1);
		goto SUB3;
		}
	}

//END TREE 3//
//
//BEGIN TREE 4//

SUB4:
	if(strcmp(opt1, "4")==0){
	if(var3 == 1){
	system("clear");
	printf("\nThe Plains v0.11\n\n");
	if(var4 == 1){
	printf("OPT1 = %s, NAV1 = %s, VAR1 = %d\nVAR2 = %d, VAR3 = %d, VAR4 = %d\n\n", opt1, nav1, var1, var2, var3, var4);
	}
	printf("\nHaving stood still for so long made you more observant.\nYou see something up in the sky...\n\n");
	printf("LOOK TO THE SKY [1]\n");
	printf("\n\nACTION >> ");
	memset(nav1, '\0', 50);
	scanf("%s", nav1);
		if(strcmp(nav1, "1")==0){
			memset(nav1, '\0', 50);
			printf("\nA spaceship that looks much like yours lands down on the surface of this strange world.\nGrass gets blown everywhere, and as it lands, you see your friends walk out.\n");
			sleep(4);
			printf("\nTO BE CONTINUED...\n");
			sleep(3);
			system("clear");
			printf("\n==TRUE ENDING==\n");
			sleep(2);
			system("clear");
			printf("\n==THANK YOU==\n==FOR PLAYING!==\n");
			sleep(2);
			return 0;
		}
		else {
		goto SUB4;
		}
	}
	if(var3 == 0){
	printf("\nDid you mean something else?\n");
	sleep(1);
			goto MAINMENU;
	}}


//BEGIN HANDLER//

	else {
	printf("\nDid you mean something else?\n");
	sleep(1);
	goto MAINMENU;
	}

//END HANDLER//
//
//END MAIN//		

}

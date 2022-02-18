#include <stdio.h>
#include <stdlib.h>
#include <curses.h>
#include <unistd.h>

#include "./../header/screen_manip.h"

void crashland_head() {
	move(1, 0);
	printw("The Plains v0.26");
	move(3, 0);
	printw("You are Liam. An astronaut by trade, you took a bad turn on the");
	move(4, 0);
	printw("Space Belt, and crash-landed on this strange, alien planet.");
	move(5, 0);
	printw("You awaken, lain on a vast field of grass.");
	move(0, 0);
}

void land_test() {
	screen_up();
	int game_loop = 0;
	int game_loop2 = 0;
	int active_x = 0;
	int active_y = 7;
	char* sel_txt[4] = {"[HILL ]", "[CAVE ]", "[TOOLS]", "[QUIT ]"};
	crashland_head();
	move(7, 0);
	printw("%s", sel_txt[0]);
	move(8, 0);
	printw("%s", sel_txt[1]);
	active_y = 9;
	move(active_y, 0);
	printw("%s", sel_txt[2]);
	active_y = 10;
	move(active_y, 0);
	printw("%s", sel_txt[3]);
	active_y = 7;
	active_x = 8;
	while (game_loop == 0) {
		while (game_loop2 == 0) {
			move(active_y, active_x);
			printw("<");
			refresh();
			switch (getch()) {
				case 'q':
					screen_down();
					exit(0);
				case KEY_UP:
				case 'w':
				case 'i':
					mvdelch(active_y, active_x);
					if (active_y == 7) {
						active_y = 10;
					} else {
						active_y -= 1;
					}
					break;
				case KEY_DOWN:
				case 's':
				case 'k':
					mvdelch(active_y, active_x);
					if (active_y == 10) {
						active_y = 7;
					} else {
						active_y += 1;
					}
					break;
				case '\n':
					game_loop2 = 1;
					break;
			}
		}
		if (game_loop2 == 1) {
			switch (active_y) {
				case 10:
					screen_down();
					exit(0);
				default:
					game_loop2 = 0;
					game_loop = 0;
					break;
			}
		}
	}
}

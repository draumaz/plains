#include <stdio.h>
#include <stdlib.h>
#include <curses.h>

#include "../header/screen_manip.h"

#ifndef CTRL // TODO move into a header file
#define CTRL(c) ((c) & 037)
#endif

void crashland_head() {
	char* star[4] = {"The Plains v0.26",
					 "You are Liam. An astronaut by trade, you took a bad turn",
					 "on the Space Belt, and crash-landed on this strange,",
					 "alien planet. You awaken, lain in a vast field of grass."
	};
	int j = 0;
	for (int i = 1; i < 6; i++) {
		if (i == 2) {
			continue;
		}
		move(i, 0);
		printw("%s", star[j]);
		j++;
	}
	move(0, 0);
}

void land_test() {
	int game_loop = 0;
	int game_loop2 = 0;
	int j = 0;
	char* sel_txt[4] = {"[HILL ]", 
						"[CAVE ]",
						"[TOOLS]",
						"[QUIT ]"
	};
	screen_up();
	crashland_head();
	for (int i = 7; i < 11; i++) {
		move(i, 0);
		printw("%s", sel_txt[j]);
		j++;
	}
	int active_y = 7;
	int active_x = 8;
	while (game_loop == 0) {
		while (game_loop2 == 0) {
			move(active_y, active_x);
			printw("<");
			refresh();
			switch (getch()) {
				case 'q':
				case CTRL('q'):
				case CTRL('c'):
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
		switch (active_y) {
			case 10:
				screen_down();
				exit(0);
			default:
				game_loop2 = 0;
				break;
		}
	}
}

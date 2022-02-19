#include <stdio.h>
#include <stdlib.h>
#include <curses.h>

#include "../header/glob_vars.h"
#include "../header/glob_vis.h"
#include "../header/screen_manip.h"
#include "../header/savesys.h"
#include "../header/c1_txt.h"

void landing_site() {
	int game_loop = 0;
	int game_loop2 = 0;
	int j = 0;
	char* sel_txt[4] = {"[HILL ]",
	"[CAVE ]",
	"[TOOLS]",
	"[QUIT ]"};
	save_exists();
	screen_up();
	tippy_head();
	landing_site_head();
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
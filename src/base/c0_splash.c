#include <stdio.h>
#include <stdlib.h>
#include <curses.h>

#include "../header/glob_vars.h"
#include "../header/glob_vis.h"
#include "../header/screen_manip.h"
#include "../header/savesys.h"
#include "../header/c1_areas.h"
#include "../header/c0_splash.h"

void splash_head() {
	char* star[3] = {"==THE PLAINS===============",
	"==DRAUMAZ, 2021-2022=======",
	"==WRITTEN IN C!============"
	};
	int j = 0;
	for (int i = SPLASH_HEAD_MIN; i < SPLASH_HEAD_MAX; i++) {
		move(i, 0);
		printw("%s",star[j]);
		j++;
	}
	move(0, 0);
}

void splash_screen() {
	int game_loop = 0;
	int game_loop2 = 0;
	int active_y = SPLASH_OPTS_MIN;
	int active_x = 8;
	int j = 0;
	char* sel_txt[3] = {"[PLAY ]", "[RESET]", "[QUIT ]"};
	screen_up();
	splash_head();
	for (int i = SPLASH_OPTS_MIN; i < SPLASH_OPTS_MAX; i++) {
		move(i, 0);
		printw("%s", sel_txt[j]);
		j++;
	}
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
					if (active_y == SPLASH_OPTS_MIN) {
						active_y = SPLASH_OPTS_MAX-1;
					} else {
						active_y -= 1;
					}
					break;
				case KEY_DOWN:
				case 's':
				case 'k':
					mvdelch(active_y, active_x);
					if (active_y == SPLASH_OPTS_MAX-1) {
						active_y = SPLASH_OPTS_MIN;
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
			case 5:
				save_exists();
				the_wiper(SPLASH_HEAD_MIN, SPLASH_HEAD_MAX-1);
				the_wiper(SPLASH_OPTS_MIN, SPLASH_OPTS_MAX-1);
				landing_site();
				break;
			case 6:
				game_loop2 = 0;
				break;
			case 7:
				screen_down();
				exit(0);
				break;
		}
	}
}
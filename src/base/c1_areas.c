#include <stdio.h>
#include <stdlib.h>
#include <curses.h>

#include "../header/c1_areas.h"

#include "../header/glob_vars.h"
#include "../header/glob_vis.h"
#include "../header/screen_manip.h"
#include "../header/savesys.h"
#include "../header/c1_txt.h"
#include "../header/c0_splash.h"

void cave() {
	int game_loop = 0;
	int game_loop2 = 0;
	int active_y = CAVE_OPTS_MIN;
	int active_x = 11;
	int j = 0;
	char* sel_txt[4] = {"[GO FORTH]",
	"[INSPECT ]",
	"[CORNER  ]",
	"[BACK    ]"};
	tippy_head();
	cave_head();
	for (int i = CAVE_OPTS_MIN; i < CAVE_OPTS_MAX; i++) {
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
					if (active_y == CAVE_OPTS_MIN) {
						active_y = CAVE_OPTS_MAX-1;
					} else {
						active_y -= 1;
					}
					break;
				case KEY_DOWN:
				case 's':
				case 'k':
					mvdelch(active_y, active_x);
					if (active_y == CAVE_OPTS_MAX-1) {
						active_y = CAVE_OPTS_MIN;
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
			case 9:
				the_wiper(CAVE_HEAD_MIN, CAVE_HEAD_MAX);
				the_wiper(CAVE_OPTS_MIN, CAVE_OPTS_MAX);
				landing_site();
				break;
			default:
				game_loop2 = 0;
				break;
		}
	}
}

void landing_site() {
	int game_loop = 0;
	int game_loop2 = 0;
	int active_y = LANDING_SITE_OPTS_MIN;
	int active_x = 8;
	int j = 0;
	char* sel_txt[4] = {"[HILL ]",
	"[CAVE ]",
	"[TOOLS]",
	"[QUIT ]"};
	tippy_head();
	landing_site_head();
	for (int i = LANDING_SITE_OPTS_MIN; i < LANDING_SITE_OPTS_MAX; i++) {
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
					if (active_y == LANDING_SITE_OPTS_MIN) {
						active_y = LANDING_SITE_OPTS_MAX-1;
					} else {
						active_y -= 1;
					}
					break;
				case KEY_DOWN:
				case 's':
				case 'k':
					mvdelch(active_y, active_x);
					if (active_y == LANDING_SITE_OPTS_MAX-1) {
						active_y = LANDING_SITE_OPTS_MIN;
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
			case 8:
				the_wiper(LANDING_SITE_HEAD_MIN, LANDING_SITE_HEAD_MAX);
				the_wiper(LANDING_SITE_OPTS_MIN, LANDING_SITE_OPTS_MAX);
				cave();
				break;
			case 10:
				the_wiper(LANDING_SITE_HEAD_MIN, LANDING_SITE_HEAD_MAX);
				the_wiper(LANDING_SITE_OPTS_MIN, LANDING_SITE_OPTS_MAX);
				splash_screen();
				break;
			default:
				game_loop2 = 0;
				break;
		}
	}
}
#include <stdio.h>
#include <stdlib.h>
#include <curses.h>

#include "../header/c0_splash.h"

#include "../header/glob_vars.h"
#include "../header/glob_vis.h"
#include "../header/screen_manip.h"
#include "../header/savesys.h"
#include "../header/c1_areas.h"

struct c0s_game {
	int head_loop;
	int body_loop;
	int active_x;
	int active_y;
	int disp_inc;
};

void splash_reset() {
	struct c0s_game c;
	c.active_x = 0;
	c.active_y = 0;
	c.head_loop = 0;
	c.body_loop = 0;
	move(SPLASH_RESET_MSG, 0);
	if (save_ephemerance() == 1) {
		printw("No save file to speak of.");
		refresh();
		scr_sleep(250);
		the_wiper(SPLASH_RESET_MSG, SPLASH_RESET_MSG+1);
		return;
	} else {
		printw("Are you sure you want to reset?");
		move(SPLASH_RESET_OPTS_MIN, 0);
		printw("[YES]");
		move(SPLASH_RESET_OPTS_MAX, 0);;
		printw("[NO ]");
		c.active_y = SPLASH_RESET_OPTS_MIN;
		c.active_x = 6;
		while (c.head_loop == 0) {
			while (c.body_loop == 0) {
				move(c.active_y, c.active_x);
				printw("<");
				refresh();
				switch (getch()) {
					case 'q':
					case CTRL('q'):
					case CTRL('c'):
						screen_down();
						exit(0);
						return;
					case KEY_UP:
					case 'w':
					case 'i':
						mvdelch(c.active_y, c.active_x);
						if (c.active_y == SPLASH_RESET_OPTS_MAX) {
							c.active_y = SPLASH_RESET_OPTS_MIN;
						} else {
							c.active_y += 1;
						}
						break;
					case KEY_DOWN:
					case 's':
					case 'k':
						mvdelch(c.active_y, c.active_x);
						if (c.active_y == SPLASH_RESET_OPTS_MIN) {
							c.active_y = SPLASH_RESET_OPTS_MAX;
						} else {
							c.active_y -= 1;
						}
						break;
					case '\n':
						c.body_loop = 1;
						break;
					default:
						break;
					}
			}
			switch (c.active_y) {
				case SPLASH_RESET_OPTS_MIN:
					move(SPLASH_RESET_OPTS_MAX+2, 0);
					if (remove("data.txt") == 0) {
						printw("Success.");
						save_exists();
						save_writer(1, 1);
					} else {
						printw("I/O error. What have you done.");
					}
					refresh();
					scr_sleep(250);
					the_wiper(SPLASH_RESET_MSG, SPLASH_RESET_OPTS_MAX+3);
					refresh();
					return;
				case SPLASH_RESET_OPTS_MAX:
					the_wiper(SPLASH_RESET_MSG, SPLASH_RESET_MSG+1);
					the_wiper(SPLASH_RESET_OPTS_MIN, SPLASH_RESET_OPTS_MAX+3);
					return;
			}
		}
	}
}

void splash_head() {
	char* star[3] = {"==THE PLAINS===============",
	"==DRAUMAZ, 2021-22=========",
	"==WRITTEN IN C!============"
	};
	int j = 0;
	for (int i = SPLASH_HEAD_MIN; i < SPLASH_HEAD_MAX+1; i++) {
		move(i, 0);
		printw("%s",star[j]);
		j++;
	}
	move(0, 0);
}

void splash_screen() {
	struct c0s_game c;
	c.head_loop = 0;
	c.body_loop = 0;
	c.active_y = SPLASH_OPTS_MIN;
	c.active_x = 10;
	c.disp_inc = 0;
	char* sel_txt[4] = {"[PLAY   ]", "[RESET  ]", "[LICENSE]","[QUIT   ]"};
	screen_up();
	splash_head();
	for (int i = SPLASH_OPTS_MIN; i < SPLASH_OPTS_MAX+1; i++) {
		move(i, 0);
		printw("%s", sel_txt[c.disp_inc]);
		c.disp_inc++;
	}
	while (c.head_loop == 0) {
		while (c.body_loop == 0) {
			move(c.active_y, c.active_x);
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
					mvdelch(c.active_y, c.active_x);
					if (c.active_y == SPLASH_OPTS_MIN) {
						c.active_y = SPLASH_OPTS_MAX;
					} else {
						c.active_y -= 1;
					}
					break;
				case KEY_DOWN:
				case 's':
				case 'k':
					mvdelch(c.active_y, c.active_x);
					if (c.active_y == SPLASH_OPTS_MAX) {
						c.active_y = SPLASH_OPTS_MIN;
					} else {
						c.active_y += 1;
					}
					break;
				case '\n':
					c.body_loop = 1;
					break;
			}
		}
		switch (c.active_y) {
			case SPLASH_OPTS_MIN: {
				save_exists();
				int * sav = save_reader();
				switch (sav[6]) {
					case 0:
						the_wiper(SPLASH_HEAD_MIN, SPLASH_HEAD_MAX+1);
						the_wiper(SPLASH_OPTS_MIN, SPLASH_OPTS_MAX+1);
						landing_site();
						break;
					case 1:
						move(SPLASH_OPTS_MAX+2, 0);
						printw("Chapter two is not quite ready yet!");
						refresh();
						scr_sleep(1000);
						move(SPLASH_OPTS_MAX+3, 0);
						printw("Feel free to reset your save to go back in.");
						refresh();
						scr_sleep(1000);
						the_wiper(SPLASH_OPTS_MAX+2, SPLASH_OPTS_MAX+4);
						c.body_loop = 0;
						break;
					default:
						c.body_loop = 0;
						break;
				}
				break; }
			case SPLASH_OPTS_MIN+1:
				splash_reset();
				c.body_loop = 0;
				break;
			case SPLASH_OPTS_MIN+2:
				move(SPLASH_OPTS_MAX+2, 0);
				printw("The Plains is free software, released under");
				move(SPLASH_OPTS_MAX+3, 0);
				printw("the GNU General Public License, version 3.");
				move(c.active_y, c.active_x);
				refresh();
				scr_sleep(2000);
				the_wiper(SPLASH_OPTS_MAX+2, SPLASH_OPTS_MAX+4);
				c.body_loop = 0;
				break;
			case SPLASH_OPTS_MAX:
				screen_down();
				exit(0);
				break;
		}
	}
}
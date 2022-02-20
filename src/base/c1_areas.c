#include <stdio.h>
#include <stdlib.h>
#include <curses.h>

#include "../header/c1_areas.h"

#include "../header/c1_txt.h"
#include "../header/c1_cave_subs.h"

#include "../header/c0_splash.h"

#include "../header/glob_vars.h"
#include "../header/glob_vis.h"
#include "../header/screen_manip.h"
#include "../header/savesys.h"

struct c1a_game {
	int head_loop;
	int body_loop;
	int active_x;
	int active_y;
	int disp_inc;
};

void cave() {
	struct c1a_game c;
	c.head_loop = 0;
	c.body_loop = 0;
	c.active_y = CAVE_OPTS_MIN;
	c.active_x = 11;
	c.disp_inc = 0;
	char* sel_txt[4] = {"[CONTINUE]",
	"[ADMIRE  ]",
	"[GO LEFT ]",
	"[BACK    ]"};
	cave_head();
	for (int i = CAVE_OPTS_MIN; i < CAVE_OPTS_MAX+1; i++) {
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
					if (c.active_y == CAVE_OPTS_MIN) {
						c.active_y = CAVE_OPTS_MAX;
					} else {
						c.active_y -= 1;
					}
					break;
				case KEY_DOWN:
				case 's':
				case 'k':
					mvdelch(c.active_y, c.active_x);
					if (c.active_y == CAVE_OPTS_MAX) {
						c.active_y = CAVE_OPTS_MIN;
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
			case 6:
				the_wiper(CAVE_HEAD_MIN, CAVE_HEAD_MAX+1);
				the_wiper(CAVE_OPTS_MIN, CAVE_OPTS_MAX+1);
				cave_subs_continue();
				break;
			case 7:
				move(11, 0);
				if (save_reader()[19] <= 7) {
					save_writer(19, save_reader()[19]+1);
				}
				switch (save_reader()[19]) {
					case 2:
						printw("...a pretty dark one, at that.");
						break;
					case 3:
						printw("Definitely a cave we've got here.");
						break;
					case 4:
						printw("But is it, really?");
						break;
					case 5:
						printw("No one may ever truly know.");
						break;
					case 6:
						printw("But I know one thing...");
						break;
					case 7:
						printw("Why are you still doing this?");
						break;
					case 1:
					default:
						printw("...sure is a cave.");
						break;
				}
				refresh();
				scr_sleep(500);
				move(11, 0);
				printw("\n");
				c.body_loop = 0;
				break;
			case 9:
				the_wiper(CAVE_HEAD_MIN, CAVE_HEAD_MAX+1);
				the_wiper(CAVE_OPTS_MIN, CAVE_OPTS_MAX+1);
				landing_site();
				break;
			default:
				c.body_loop = 0;
				break;
		}
	}
}

void landing_site() {
	struct c1a_game c;
	c.head_loop = 0;
	c.body_loop = 0;
	c.active_y = LANDING_SITE_OPTS_MIN;
	c.active_x = 8;
	c.disp_inc = 0;
	char* sel_txt[4] = {"[HILL ]",
	"[CAVE ]",
	"[TOOLS]",
	"[QUIT ]"};
	tippy_head();
	landing_site_head();
	for (int i = LANDING_SITE_OPTS_MIN; i < LANDING_SITE_OPTS_MAX+1; i++) {
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
					if (c.active_y == LANDING_SITE_OPTS_MIN) {
						c.active_y = LANDING_SITE_OPTS_MAX;
					} else {
						c.active_y -= 1;
					}
					break;
				case KEY_DOWN:
				case 's':
				case 'k':
					mvdelch(c.active_y, c.active_x);
					if (c.active_y == LANDING_SITE_OPTS_MAX) {
						c.active_y = LANDING_SITE_OPTS_MIN;
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
			case 8:
				the_wiper(LANDING_SITE_HEAD_MIN, LANDING_SITE_HEAD_MAX+1);
				the_wiper(LANDING_SITE_OPTS_MIN, LANDING_SITE_OPTS_MAX+1);
				cave();
				break;
			case 10:
				the_wiper(LANDING_SITE_HEAD_MIN, LANDING_SITE_HEAD_MAX+1);
				the_wiper(LANDING_SITE_OPTS_MIN, LANDING_SITE_OPTS_MAX+1);
				splash_screen();
				break;
			default:
				c.body_loop = 0;
				break;
		}
	}
}
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

void splash_head() {
	char* star[3] = {"==THE PLAINS===============",
	"==DRAUMAZ, 2021-2022=======",
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
	c.active_x = 8;
	c.disp_inc = 0;
	char* sel_txt[3] = {"[PLAY ]", "[RESET]", "[QUIT ]"};
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
			case 5:
				save_exists();
				the_wiper(SPLASH_HEAD_MIN, SPLASH_HEAD_MAX+1);
				the_wiper(SPLASH_OPTS_MIN, SPLASH_OPTS_MAX+1);
				landing_site();
				break;
			case 6:
				c.body_loop = 0;
				break;
			case 7:
				screen_down();
				exit(0);
				break;
		}
	}
}
#include <stdio.h>
#include <stdlib.h>
#include <curses.h>

#include "../header/c1_cave_subs.h"

#include "../header/c1_areas.h"
#include "../header/glob_vars.h"
#include "../header/glob_vis.h"
#include "../header/screen_manip.h"
#include "../header/savesys.h"
#include "../header/c1_txt.h"

struct c1c_subs {
	int head_loop;
	int body_loop;
	int active_x;
	int active_y;
	int disp_inc;
};

void cave_subs_goleft() {
	struct c1c_subs c;
	c.head_loop = 0;
	c.body_loop = 0;
	c.disp_inc = 0;
	c.active_y = CAVE_SUBS_CONTINUE_OPTS_MIN;
	int has_bottle = save_reader()[3];
	char* head_txt;
	char* sel_txt[2];
	switch (has_bottle) {
		case 0:
		case 2:
			if (has_bottle == 0) { head_txt = "Another locked chest! This one's covered in dirt."; }
			if (has_bottle == 2) { head_txt = "What a gross chest. Does nobody keep tidy here?"; }
			sel_txt[0] = "[OPEN]";
			sel_txt[1] = "[BACK]";
			c.active_x = 7;
			break;
		case 1:
			head_txt = "That chest sucks, but this bottle seems useful.";
			sel_txt[0] = "[RETURN ]";
			sel_txt[1] = "[GO BACK]";
			c.active_x = 10;
			break;
	}
	for (int i = CAVE_SUBS_CONTINUE_OPTS_MIN; i < CAVE_SUBS_CONTINUE_OPTS_MAX+1; i++) {
		move(i, 0);
		printw("%s", sel_txt[c.disp_inc]);
		c.disp_inc++;
	}
	move(3, 0);
	printw("%s", head_txt);
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
					if (c.active_y == CAVE_SUBS_CONTINUE_OPTS_MIN) {
						c.active_y = CAVE_SUBS_CONTINUE_OPTS_MAX;
					} else {
						c.active_y -= 1;
					}
					break;
				case KEY_DOWN:
				case 's':
				case 'k':
					mvdelch(c.active_y, c.active_x);
					if (c.active_y == CAVE_SUBS_CONTINUE_OPTS_MAX) {
						c.active_y = CAVE_SUBS_CONTINUE_OPTS_MIN;
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
				move(8, 0);
				switch (has_bottle) {
					case 0:
						save_writer(3, 1);
						printw("Woah, an empty bottle! You take it.");
						break;
					case 1:
						save_writer(3, 2);
						printw("You put the bottle back.");
						break;
					case 2:
						save_writer(3, 1);
						printw("You take the bottle back.");
						break;
				}
				the_wiper(TIPPY_HEAD_MIN, TIPPY_HEAD_MAX);
				tippy_head();
				refresh();
				scr_sleep(500);
				the_wiper(3, CAVE_SUBS_CONTINUE_OPTS_MAX+3);
				cave_subs_goleft();
				break;
			case 6:
				the_wiper(3, CAVE_SUBS_CONTINUE_OPTS_MAX+1);
				the_wiper(CAVE_SUBS_CONTINUE_OPTS_MIN, CAVE_SUBS_CONTINUE_OPTS_MAX);
				cave();
				break;
			default:
				c.body_loop = 0;
				break;
		}
	}
}

void cave_subs_continue() {
	struct c1c_subs c;
	c.head_loop = 0;
	c.body_loop = 0;
	c.disp_inc = 0;
	c.active_y = CAVE_SUBS_CONTINUE_OPTS_MIN;
	int has_knife = save_reader()[0];
	char* head_txt;
	char* sel_txt[2];
	switch (has_knife) {
		case 0:
		case 2:
			if (has_knife == 0) { head_txt = "You continue deeper. A chest sits against the stone."; }
			if (has_knife == 2) { head_txt = "There's that knife-filled chest again."; }
			sel_txt[0] = "[OPEN]";
			sel_txt[1] = "[BACK]";
			c.active_x = 7;
			break;
		case 1:
			head_txt = "An empty chest lies beneath the darkness.";
			sel_txt[0] = "[RETURN ]";
			sel_txt[1] = "[GO BACK]";
			c.active_x = 10;
			break;
	}
	for (int i = CAVE_SUBS_CONTINUE_OPTS_MIN; i < CAVE_SUBS_CONTINUE_OPTS_MAX+1; i++) {
		move(i, 0);
		printw("%s", sel_txt[c.disp_inc]);
		c.disp_inc++;
	}
	move(3, 0);
	printw("%s", head_txt);
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
					if (c.active_y == CAVE_SUBS_CONTINUE_OPTS_MIN) {
						c.active_y = CAVE_SUBS_CONTINUE_OPTS_MAX;
					} else {
						c.active_y -= 1;
					}
					break;
				case KEY_DOWN:
				case 's':
				case 'k':
					mvdelch(c.active_y, c.active_x);
					if (c.active_y == CAVE_SUBS_CONTINUE_OPTS_MAX) {
						c.active_y = CAVE_SUBS_CONTINUE_OPTS_MIN;
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
				move(8, 0);
				switch (has_knife) {
					case 0:
						save_writer(0, 1);
						printw("A rusty knife! You take it.");
						break;
					case 1:
						save_writer(0, 2);
						printw("You put the knife back.");
						break;
					case 2:
						save_writer(0, 1);
						printw("You grab the knife again.");
						break;
				}
				the_wiper(TIPPY_HEAD_MIN, TIPPY_HEAD_MAX);
				tippy_head();
				refresh();
				scr_sleep(500);
				the_wiper(3, CAVE_SUBS_CONTINUE_OPTS_MAX+3);
				cave_subs_continue();
				break;
			case 6:
				the_wiper(3, CAVE_SUBS_CONTINUE_OPTS_MAX+1);
				the_wiper(CAVE_SUBS_CONTINUE_OPTS_MIN, CAVE_SUBS_CONTINUE_OPTS_MAX);
				cave();
				break;
		}
	}
}
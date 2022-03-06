#include <stdio.h>
#include <stdlib.h>
#include <curses.h>

#include "../header/c1_hill_subs.h"

#include "../header/c1_areas.h"
#include "../header/glob_vars.h"
#include "../header/glob_vis.h"
#include "../header/screen_manip.h"
#include "../header/savesys.h"
#include "../header/c1_txt.h"

struct c1h_subs {
	int head_loop;
	int body_loop;
	int active_x;
	int active_y;
	int disp_inc;
};

void hill_subs_mntn() {
	int * sav = save_reader();
	struct c1h_subs c;
	c.head_loop = 0;
	c.body_loop = 0;
	c.disp_inc = 0;
	c.active_y = HILL_SUBS_MNTN_OPTS_MIN;
	c.active_x = 7;
	char* sel_txt[2];
	char* head_txt[2];
	sel_txt[1] = "[BACK]";
	head_txt[0] = "A gentle wind flows through the sky.";
	if (sav[4] == 1) {
		sel_txt[0] = "[CALL]";
		head_txt[1] = "Seems like you're phone's got service up here.";
	} else {
		sel_txt[0] = "[COLD]";
		head_txt[1] = "Not a whole lot to see up here.";
	}
	for (int i = HILL_SUBS_MNTN_OPTS_MIN; i < HILL_SUBS_MNTN_OPTS_MAX+1; i++) {
		move(i, 0);
		printw("%s", sel_txt[c.disp_inc]);
		c.disp_inc++;
	}
	c.disp_inc = 0;
	for (int i = HILL_SUBS_MNTN_MSG_MIN; i < HILL_SUBS_MNTN_MSG_MAX+1; i++) {
		move(i, 0);
		printw("%s", head_txt[c.disp_inc]);
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
					if (c.active_y == HILL_SUBS_MNTN_OPTS_MIN) {
						c.active_y = HILL_SUBS_MNTN_OPTS_MAX;
					} else {
						c.active_y -= 1;
					}
					break;
				case KEY_DOWN:
				case 's':
				case 'k':
					mvdelch(c.active_y, c.active_x);
					if (c.active_y == HILL_SUBS_MNTN_OPTS_MAX) {
						c.active_y = HILL_SUBS_MNTN_OPTS_MIN;
					} else {
						c.active_y += 1;
					}
					break;
				case '\n':
					c.body_loop = 1;
					break;
			}
		}
		sav = save_reader();
		switch (c.active_y) {
			case HILL_SUBS_MNTN_OPTS_MIN:
				if (sav[5] == 0 && sav[4] == 1) {
					save_writer(5, 1); // ch1 end flag
					move(HILL_SUBS_MNTN_SUBMSG_MIN, 0);
					printw("Brrrrr...");
					refresh();
					scr_sleep(3000);
					move(HILL_SUBS_MNTN_SUBMSG_MIN+2, 0);
					printw("'Liam! Where'd you end up?'");
					refresh();
					scr_sleep(1000);
					move(HILL_SUBS_MNTN_SUBMSG_MIN+3, 0);
					printw("...sounds like Saan! You send your coords over.");
					refresh();
					scr_sleep(2000);
					move(HILL_SUBS_MNTN_SUBMSG_MIN+5, 0);
					printw("Prrnk! ...he hung up.");
				} else if (sav[5] == 1) {
					move(HILL_SUBS_MNTN_SUBMSG_MIN, 0);
					printw("Your friends are already on the way.");
				} else {
					move(HILL_SUBS_MNTN_SUBMSG_MIN, 0);
					printw("Indeed, it is quite cold.");
				}
				refresh();
				scr_sleep(1000);
				the_wiper(HILL_SUBS_MNTN_SUBMSG_MIN, HILL_SUBS_MNTN_SUBMSG_MAX+1);
				c.body_loop = 0;
				break;
			case HILL_SUBS_MNTN_OPTS_MAX:
				the_wiper(HILL_SUBS_MNTN_OPTS_MIN, HILL_SUBS_MNTN_OPTS_MAX+1);
				the_wiper(HILL_SUBS_MNTN_MSG_MIN, HILL_SUBS_MNTN_MSG_MAX+1);
				hill();
				break;
			default:
				c.body_loop = 0;
				break;
		}
	}
}

void hill_subs_river() {
	struct c1h_subs c;
	c.head_loop = 0;
	c.body_loop = 0;
	c.disp_inc = 0;
	c.active_y = HILL_SUBS_RIVER_OPTS_MIN;
	c.active_x = 8;
	int bottle_cont = save_reader()[3];
	char* sel_txt[3];
	sel_txt[2] = "[BACK ]";
	sel_txt[0] = "[RELAX]";
	char* head_txt = "A river gently streams through this strange planet.";
	switch (bottle_cont) {
		case 0: // don't have
		case 2:
			sel_txt[1] = "[CHILL]";
			break;
		case 1: // empty
			sel_txt[1] = "[FILL ]";
			break;
		case 3: // water
			sel_txt[1] = "[EMPTY]";
			break;
	}
	for (int i = HILL_SUBS_RIVER_OPTS_MIN; i < HILL_SUBS_RIVER_OPTS_MAX+1; i++) {
		move(i, 0);
		printw("%s", sel_txt[c.disp_inc]);
		c.disp_inc++;
	}
	move(HILL_SUBS_RIVER_MSG, 0);
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
					if (c.active_y == HILL_SUBS_RIVER_OPTS_MIN) {
						c.active_y = HILL_SUBS_RIVER_OPTS_MAX;
					} else {
						c.active_y -= 1;
					}
					break;
				case KEY_DOWN:
				case 's':
				case 'k':
					mvdelch(c.active_y, c.active_x);
					if (c.active_y == HILL_SUBS_RIVER_OPTS_MAX) {
						c.active_y = HILL_SUBS_RIVER_OPTS_MIN;
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
			case HILL_SUBS_RIVER_OPTS_MIN+1:
				move(HILL_SUBS_RIVER_OPTS_MAX+2, 0);
				if (bottle_cont == 0) {
					printw("...isn't this the same thing as relaxing?");
				} else if (bottle_cont == 1) {
					save_writer(3, 3);
					printw("You collect some water into your bottle.");
				} else if (bottle_cont == 3) {
					save_writer(3, 1);
					printw("You empty your bottle out into the river.");
				} else { // should never happen
					printw("Really? Modding the save file? Lame.");
				}
				if (bottle_cont == 1 || bottle_cont == 3) {
					the_wiper(TIPPY_HEAD_MIN, TIPPY_HEAD_MAX);
					tippy_head();
				}
				refresh();
				scr_sleep(500);
				move(HILL_SUBS_RIVER_OPTS_MAX+2, 0);
				printw("\n");
				the_wiper(HILL_SUBS_RIVER_OPTS_MIN, HILL_SUBS_RIVER_OPTS_MAX+1);
				hill_subs_river();
				break;
			case HILL_SUBS_RIVER_OPTS_MAX:
				the_wiper(HILL_SUBS_RIVER_MSG, HILL_SUBS_RIVER_OPTS_MAX+1);
				hill();
				break;
			default:
				c.body_loop = 0;
				break;
		}
	}
}
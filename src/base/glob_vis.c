#include <curses.h>
#include <time.h>
#include <errno.h>
#include <ctype.h>

#include "../header/glob_vis.h"
#include "../header/glob_vars.h"

#include "../header/savesys.h"

int tippy_inv_quantity(int slot) {
	int * sav = save_reader();
	int quant = 0;
	switch (slot) {
		case 0: // knife
			switch (sav[0]) {
				case 0:
				case 2:
					quant = 0;
					break;
				case 1:
					quant = 1;
					break;
			}
			return quant;
			break;
		case 1: // bottle:
			switch (sav[3]) {
				case 0:
				case 2:
					quant = 0;
					break;
				case 1:
				case 3:
					quant = 1;
					break;
			}
			return quant;
			break;
		case 2: // phone:
			switch (sav[4]) {
				case 0:
					quant = 0;
					break;
				case 1:
				case 2:
					quant = 1;
					break;
			}
			return quant;
			break;
	}
	return ERR;
}

void tippy_inv() {
	move(TIPPY_HEAD_MIN, 17);
	printw("| INV:");
}

void tippy_knife(int o) {
	int quant = tippy_inv_quantity(0);
	int knife_var = save_reader()[0];
	char* itm = "";
	if (knife_var == 0) {
		itm = "?????";
	} else {
		itm = "KNIFE";
	}
	int x = 0;
	move(TIPPY_HEAD_MIN, 24);
	printw("%dx %s |", quant, itm);
	move(TIPPY_HEAD_MIN, x+9);
}

void tippy_bottle(int o) {
	int quant = tippy_inv_quantity(1);
	int bottle_var = save_reader()[3];
	int x = 0;
	char* itm = "";
	switch (bottle_var) {
		case 0:
			itm = "??????";
			break;
		case 3:
			itm = "BOTTLE (WTR)";
			break;
		default:
			itm = "BOTTLE";
			break;
	}
	move(TIPPY_HEAD_MIN, 46);
	printw("%dx %s", quant, itm);
	move(TIPPY_HEAD_MIN, x+9);
}

void tippy_phone(int o) {
	char* itm = "";
	int phone_var = save_reader()[4];
	if (phone_var == 0) {
		itm = "?????";
	} else {
		itm = "PHONE";
	}
	int quant = tippy_inv_quantity(2);
	int x = 0;
	move(TIPPY_HEAD_MIN, 35);
	printw("%dx %s |", quant, itm);
	move(TIPPY_HEAD_MIN, x+10);
}

void tippy_head() {
	int * sav = save_reader();
	move(TIPPY_HEAD_MIN, 0);
	printw("The Plains v%s", VERSION);
	if ((sav[0] == 1) || (sav[3] == 1) || (sav[4] == 1)) {
		tippy_inv();
		tippy_knife(0);
		tippy_bottle(1);
		tippy_phone(2);
	}
	move(0, 0);
}

void the_wiper(int min, int max) {
	for (int i = min; i < max; i++) {
		move(i, 0);
		printw("\n");
	}
}

void scr_sleep(int ms) {
	struct timespec ts;
	int res;
	if (ms < 0) { errno = EINVAL; }
	ts.tv_sec = ms / 1000;
	ts.tv_nsec = (ms % 1000) * 1000000;
	do { res = nanosleep(&ts, &ts); }
	while (res && errno == EINTR);
}
#include <curses.h>
#include <time.h>
#include <errno.h>
#include <ctype.h>

#include "../header/glob_vis.h"
#include "../header/glob_vars.h"

#include "../header/savesys.h"

int tippy_inv_quantity(int slot) {
	int quant = 0;
	switch (slot) {
		case 0: // knife
			switch (save_reader()[0]) {
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
			switch (save_reader()[3]) {
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
			switch (save_reader()[4]) {
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
	char* itm = "";
	if (save_reader()[0] == 0) {
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
	char* itm = "";
	if (save_reader()[3] == 0) {
		itm = "??????";
	} else if (save_reader()[3] == 3) {
		itm = "BOTTLE (WTR)";
	} else {
		itm = "BOTTLE";
	}
	int x = 0;
	move(TIPPY_HEAD_MIN, 46);
	printw("%dx %s", quant, itm);
	move(TIPPY_HEAD_MIN, x+9);
}

void tippy_phone(int o) {
	char* itm = "";
	if (save_reader()[4] == 0) {
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
	move(TIPPY_HEAD_MIN, 0);
	printw("The Plains v%s", VERSION);
	if (save_compare(0, 1 == 0) || save_compare(3, 1 == 0) || save_compare(4, 1 == 0)) {
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
#include <curses.h>
#include <time.h>
#include <errno.h>
#include <ctype.h>

#include "../header/glob_vis.h"
#include "../header/glob_vars.h"

#include "../header/savesys.h"

void tippy_inv() {
	move(TIPPY_HEAD_MIN, 17);
	printw("| INV:");
}

void tippy_knife(int o) {
	int quant = 0;
	switch (save_reader()[3]) {
		case 0:
		case 2:
			quant = 0;
			break;
		case 1:
			quant = 1;
			break;
	}
	int x = 0;
	switch (o) {
		case 0:
			x = 24;
			break;
		case 1:
			x = 35;
			break;
	}
	move(TIPPY_HEAD_MIN, x);
	printw("%dx KNIFE", quant);
	move(TIPPY_HEAD_MIN, x+9);
}

void tippy_bottle(int o) {
	int quant = 0;
	switch (save_reader()[3]) {
		case 0:
		case 2:
			quant = 0;
			break;
		case 1:
			quant = 1;
			break;
	}
	int x = 0;
	switch (o) {
		case 0:
			x = 24;
			break;
		case 1:
			x = 35;
			break;
	}
	move(TIPPY_HEAD_MIN, x);
	printw("%dx BOTTLE", quant);
	move(TIPPY_HEAD_MIN, x+9);
}

void tippy_head() {
	move(TIPPY_HEAD_MIN, 0);
	printw("The Plains v%s", VERSION);
	if (save_compare(0, 1) == 0 && save_compare(3, 1) == 0) { // This is not sustainable.
		tippy_inv();
		tippy_knife(0);
		printw("|");
		tippy_bottle(1);
		return;
	}
	if (save_compare(0, 1) == 1 && save_compare(3, 1) == 0) {
		tippy_inv();
		tippy_bottle(0);
		return;
	}
	if (save_compare(0, 1) == 0 && save_compare(3, 1) == 1) {
		tippy_inv();
		tippy_knife(0);
		return;
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
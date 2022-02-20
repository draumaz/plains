#include <curses.h>
#include <time.h>
#include <errno.h>
#include <ctype.h>

#include "../header/glob_vars.h"

#include "../header/savesys.h"

void tippy_head() {
	move(1, 0);
	printw("The Plains v%s", VERSION);
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
	if (ms < 0) {
		errno = EINVAL;
	}
	ts.tv_sec = ms / 1000;
	ts.tv_nsec = (ms % 1000) * 1000000;
	do {
		res = nanosleep(&ts, &ts);
	} while (res && errno == EINTR);
}
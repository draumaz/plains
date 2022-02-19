#include <curses.h>

#include "../header/glob_vars.h"

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
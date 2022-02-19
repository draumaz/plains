#include <curses.h>

#include "../header/glob_vars.h"

void tippy_head() {
	move(1, 0);
	printw("The Plains v%s", VERSION);
	move(0, 0);
}
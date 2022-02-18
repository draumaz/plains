#include <curses.h>
#include <stdlib.h>

#define CLEAN_SCREEN_LINUX "stty sane"

void screen_up() {
	initscr();
	noecho();
	curs_set(0);
	raw();
	keypad(stdscr, true);
}

void screen_down() {
	clear();
	keypad(stdscr, false);
	endwin();
	curs_set(1);
	system(CLEAN_SCREEN_LINUX);
}

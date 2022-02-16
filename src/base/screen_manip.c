#include <curses.h>
#include <stdlib.h>

#ifdef _WIN32
	#define STOP_CMD "pause"
#else
	#define STOP_CMD "stty sane"
#endif

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
	system(STOP_CMD);
}
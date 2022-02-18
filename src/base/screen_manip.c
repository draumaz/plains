#include <curses.h>
#include <stdlib.h>

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
	system("stty sane");
}

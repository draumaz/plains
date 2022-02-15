#include <stdio.h>
#include <stdlib.h>
#include <curses.h>
#include <unistd.h>

void land_test() {
	int game_loop = 0;
	int game_loop2 = 0;
	int active_x = 0;
	int active_y = 0;
	initscr();
	noecho();
	curs_set(0);
	raw();
	keypad(stdscr, true);
	active_y = 1;
	char* sel_txt[4] = {"[HILL ]", "[CAVE ]", "[TOOLS]", "[QUIT ]"};
	move(active_y, 0);
	printw("The Plains v0.26");
	active_y = 3;
	move(active_y, 0);
	printw("You are Liam. An astronaut by trade, you took a bad turn on the");
	active_y = 4;
	move(active_y, 0);
	printw("Space Belt, and crash-landed on a strange planet.");
	active_y = 5;
	move(active_y, 0);
	printw("You awaken, laying in a field of grass.");
	active_y = 7;
	move(active_y, 0);
	printw("%s", sel_txt[0]);
	active_y = 8;
	move(active_y, 0);
	printw("%s", sel_txt[1]);
	active_y = 9;
	move(active_y, 0);
	printw("%s", sel_txt[2]);
	active_y = 10;
	move(active_y, 0);
	printw("%s", sel_txt[3]);
	active_y = 7;
	active_x = 8;
	move(active_y, active_x);
	refresh();
	while (game_loop == 0) {
		move(active_y, active_x);
		printw("<");
		refresh();
		switch (getch()) {
			case 'q':
				system("stty sane");
				curs_set(1);
				exit(0);
			case KEY_UP:
			case 'w':
			case 'i':
				mvdelch(active_y, active_x);
				if (active_y == 7) {
					active_y = 10;
				} else {
					active_y -= 1;
				}
				break;
			case KEY_DOWN:
			case 's':
			case 'k':
				mvdelch(active_y, active_x);
				if (active_y == 10) {
					active_y = 7;
				} else {
					active_y += 1;
				}
				break;
		}
	}
	clear();
	keypad(stdscr, false);
	endwin();
	curs_set(1);
	system("stty sane");
}
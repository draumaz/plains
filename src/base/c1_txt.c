#include <curses.h>

#include "../header/glob_vars.h"

void landing_site_head() {
	char* star[3] = {"You are Liam. An astronaut by trade, you took a bad turn",
					"on the Space Belt, and crash-landed on this strange,",
					"alien planet. You awaken, lain in a vast field of grass."
	};
	int j = 0;
	for (int i = 3; i < 6; i++) {
		move(i, 0);
		printw("%s", star[j]);
		j++;
	}
	move(0, 0);
}

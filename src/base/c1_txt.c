#include <curses.h>

#include "../header/c1_txt.h"

#include "../header/glob_vars.h"

void landing_site_head() {
	char* star[3] = {"You are Liam. An astronaut by trade, you took a bad turn",
	"on the Space Belt, and crash-landed on this strange,",
	"alien planet. You awaken, lain in a vast field of grass."
	};
	int j = 0;
	for (int i = LANDING_SITE_HEAD_MIN; i < LANDING_SITE_HEAD_MAX; i++) {
		move(i, 0);
		printw("%s", star[j]);
		j++;
	}
	move(0, 0);
}

void cave_head() {
	char* star[2] = {"You make your way towards a deep, cavernous grotto.",
	"You can barely make anything out past the entrance."
	};
	int j = 0;
	for (int i = CAVE_HEAD_MIN; i < CAVE_HEAD_MAX; i++) {
		move(i, 0);
		printw("%s", star[j]);
		j++;
	}
	move(0, 0);
}
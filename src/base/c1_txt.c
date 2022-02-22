#include <curses.h>

#include "../header/c1_txt.h"

#include "../header/glob_vars.h"

void landing_site_head() {
	char* star[3] = {"You are Liam. An astronaut by trade, you took a bad",
	"turn on the Space Belt, and crash-landed on this strange,",
	"alien planet. You awaken, lain in a vast field of grass."
	};
	int j = 0;
	for (int i = LANDING_SITE_HEAD_MIN; i < LANDING_SITE_HEAD_MAX+1; i++) {
		move(i, 0);
		printw("%s", star[j]);
		j++;
	}
	move(0, 0);
}

void ship_dig_head() {
	char* star[2] = {"You dig around, and find your busted-up cell phone!",
	"Will you take it?"};
	int j = 0;
	for (int i = SHIP_DIG_HEAD_MIN; i < SHIP_DIG_HEAD_MAX+1; i++) {
		move(i, 0);
		printw("%s", star[j]);
		j++;
	}
}

void ship_head() {
	char* star[3] = {"You make your way back to your ship - or at least",
	"what's left of it. Everything is covered in wires,",
	"broken machinery, and a strange, ashy substance."
	};
	int j = 0;
	for (int i = SHIP_HEAD_MIN; i < SHIP_HEAD_MAX+1; i++) {
		move(i, 0);
		printw("%s", star[j]);
		j++;
	}
}

void cave_head() {
	char* star[2] = {"You make your way towards a deep, cavernous grotto.",
	"You can barely make anything out past the entrance."
	};
	int j = 0;
	for (int i = CAVE_HEAD_MIN; i < CAVE_HEAD_MAX+1; i++) {
		move(i, 0);
		printw("%s", star[j]);
		j++;
	}
	move(0, 0);
}

void hill_head() {
	char* star[2] = {"You venture out towards a gargantuan hill.",
	"Beside it runs a stream of quickly-flowing water."
	};
	int j = 0;
	for (int i = HILL_HEAD_MIN; i < HILL_HEAD_MAX+1; i++) {
		move(i, 0);
		printw("%s", star[j]);
		j++;
	}
	move(0, 0);
}
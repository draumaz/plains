use crate::routine::{funk::{universal_tabler, screen_smash}, flourish::display_header, misc::sleep};

fn hill_page_text(win: &pancurses::Window) {
	win.mv(3, 0);
	win.printw("You venture out towards a gargantuan hill.\nBeside it runs a stream of quickly-flowing water.\n\n[USE PHONE]\n[MOUNTAIN ]\n[TO RIVER ]\n[BACK     ]");
}

fn hill_page(win: &pancurses::Window) {
	loop {
		hill_page_text(&win);
		match universal_tabler(&win, 6, 9, 12) {
			6|7|8 => {continue}
			9|_ => {
				screen_smash(&win, 3, 9);
				break;
			}
		}
	}
}

fn landing_site_text(win: &pancurses::Window) {
	win.mv(3, 0);
	win.printw("You are Liam. An astronaut by trade, you took a bad\nturn on the Space Belt, and crash-landed on this strange,\nalien planet. You awaken, lain in a vast field of grass.\n\n[HILL]\n[CAVE]\n[SHIP]\n[QUIT]");
}

pub fn landing_site(win: &pancurses::Window) {
	loop {
		landing_site_text(&win);
		match universal_tabler(&win, 7, 10, 7) {
			7 => {
				screen_smash(&win, 3, 10);
				hill_page(&win);
				}
			8|9 => {continue}
			10|_ => {
				screen_smash(&win, 0, 10);
				break;
			}
		}
	}
}

fn splash_text(win: &pancurses::Window) {
	win.mv(1, 0);
	win.printw("==THE PLAINS===============\n==DRAUMAZ, 2021-22=========\n==WRITTEN IN RUST!=========");
	win.mv(5, 0);
	win.printw("[PLAY   ]\n[RESET  ]\n[LICENSE]\n[QUIT   ]");
}

pub fn splash_screen(win: &pancurses::Window) {
	loop {
		splash_text(&win);
		match universal_tabler(&win, 5, 8, 11) {
			5 => {
				screen_smash(&win, 0, 11);
				display_header(&win);
				landing_site(&win);
				screen_smash(&win, 0, 11);
				splash_text(&win);
				continue;
			}
			6 => {continue}
			7 => {
				win.mv(10, 0);
				win.printw("Copyright 2021-22 draumaz.\nAll rights reserved.");
				win.refresh();
				sleep(1000);
				screen_smash(&win, 10, 11);
				continue;
			}
			8|_ => {break}
		}
	}
}

use crate::routine::funk::{universal_tabler, screen_smash};

fn hill_page_text(win: &pancurses::Window) {
	win.mv(3, 0);
	win.printw("You venture out towards a gargantuan hill.\nBeside it runs a stream of quickly-flowing water.\n\n[USE PHONE]\n[MOUNTAIN ]\n[TO RIVER ]\n[BACK     ]");
}

fn hill_page(win: &pancurses::Window) {
	loop {
		hill_page_text(&win);
		match universal_tabler(&win, 6, 9, 12, 6) {
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
		match universal_tabler(&win, 7, 10, 7, 7) {
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

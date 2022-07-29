use crate::routine::{funk::{universal_tabler, screen_smash}, flourish::display_header, misc::sleep};
use savesys::{exists, generate, reader};

fn river_page(win: &pancurses::Window) {
	let mode = reader("data.txt")[4];
	loop {
		win.mv(3, 0);
		win.printw("A river juts through the landscape.");
		win.mv(5, 0);
		match mode {
			1 => {
				win.printw("[RELAX]\n[FILL ]\n[BACK ]");
			}
			3 => {
				win.printw("[RELAX]\n[EMPTY]\n[BACK ]");
			}
			2|_ => {
				win.printw("[RELAX]\n[CHILL]\n[BACK ]");
			}
		}
		match universal_tabler(&win, 5, 7, 8) {
			5 => {}
			6 => {
				match mode {
					_ => {}
				}
			}
			7|_ => {break}
		}
	}
}

fn mountain_page(win: &pancurses::Window) {
	loop {
		win.mv(3, 0);
		win.printw("A gentle wind flows through the sky.");
		win.mv(4, 0);
		match reader("data.txt")[4] {
			1 => {
				win.printw("Seems like your phone's got service.");
		    	win.mv(6, 0); win.printw("[CALL]\n[BACK]");
			}
			_ => {
				win.printw("Not much to see up here.");
				win.mv(6, 0); win.printw("[COLD]\n[BACK]");
			}
		}
		match universal_tabler(&win, 6, 7, 7) {
			6 => {
				match reader("data.txt")[4] {
					0 => {
						win.mv(9, 0);
						win.printw("Indeed, it's quite cold up here.");
						win.refresh();
						sleep(1000);
						screen_smash(&win, 9, 9);
					}
					_ => {}
				}
				continue;
			}
			7|_ => {
				screen_smash(&win, 3, 7);
				break;
			}
		}
	}
}

fn hill_page(win: &pancurses::Window) {
	loop {
		win.mv(3, 0);
		win.printw("You venture out towards a gargantuan hill.\nBeside it runs a stream of quickly-flowing water.\n\n[USE PHONE]\n[MOUNTAIN ]\n[TO RIVER ]\n[BACK     ]");
		match universal_tabler(&win, 6, 9, 12) {
			6 => {
				match reader("data.txt")[4] {
					0 => {
						win.mv(11, 0);
						win.printw("Seems like you lost your phone in the crash.");
						win.refresh();
						sleep(1000);
						screen_smash(&win, 11, 11);
					}
					_ => {}
				}
			}
			7 => {
				screen_smash(&win, 3, 9);
				mountain_page(&win);
			}
			8 => {
				screen_smash(&win, 3, 9);
				river_page(&win);
			}
			9|_ => {
				screen_smash(&win, 3, 9);
				break;
			}
		}
	}
}

fn landing_site(win: &pancurses::Window) {
	loop {
		win.mv(3, 0);
		win.printw("You are Liam. An astronaut by trade, you took a bad\nturn on the Space Belt, and crash-landed on this strange,\nalien planet. You awaken, lain in a vast field of grass.\n\n[HILL]\n[CAVE]\n[SHIP]\n[QUIT]");
		match universal_tabler(&win, 7, 10, 7) {
			7 => {
				screen_smash(&win, 3, 10);
				hill_page(&win);
			}
			8|9 => {}
			10|_ => {
				screen_smash(&win, 0, 10);
				break;
			}
		}
	}
}

pub fn splash_screen(win: &pancurses::Window) {
	loop {
		win.mv(1, 0);
		win.printw("==THE PLAINS===============\n==DRAUMAZ, 2021-22=========\n==WRITTEN IN RUST!=========");
		win.mv(5, 0);
		win.printw("[PLAY   ]\n[RESET  ]\n[LICENSE]\n[QUIT   ]");
		match universal_tabler(&win, 5, 8, 11) {
			5 => {
				if ! exists("data.txt") { generate("data.txt", 20) }
				screen_smash(&win, 0, 11);
				display_header(&win);
				landing_site(&win);
				screen_smash(&win, 0, 11);
			}
			6 => {}
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

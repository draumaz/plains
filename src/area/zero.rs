use crate::routine::{funk::{table_seek, screen_smash}, flourish::{display_header, obo_blitter}, misc::sleep};
use savesys::{exists, generate, reader, writer};
use std::fs::remove_file;

fn hill_river_page(win: &pancurses::Window) {
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
		match table_seek(&win, 5, 7, 8) {
			5 => {
				win.mv(9, 0);
				win.printw("You sit down a spell and take in the nature.");
				win.refresh();
				sleep(1500);
				win.mv(10, 0);
				win.printw("How calming!");
				win.refresh();
				sleep(1000);
				screen_smash(&win, 9, 10);
			}
			6 => {
				match mode {
					1 => {}
					3 => {}
					2|_ => {
						win.mv(9, 0);
						win.printw("This is basically the same thing as relaxing, right?");
						win.refresh();
						sleep(1000);
						screen_smash(&win, 9, 9);
					}
				}
			}
			7|_ => {break}
		}
	}
}

fn hill_mountain_page(win: &pancurses::Window) {
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
		match table_seek(&win, 6, 7, 7) {
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
		match table_seek(&win, 6, 9, 12) {
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
				hill_mountain_page(&win);
			}
			8 => {
				screen_smash(&win, 3, 9);
				hill_river_page(&win);
			}
			9|_ => {
				screen_smash(&win, 3, 9);
				break;
			}
		}
	}
}

fn cave_continue_page(win: &pancurses::Window) {
	let mut pos: i32;
	loop {
		win.mv(3, 0);
		match reader("data.txt")[0] {
			0|2 => {
				match reader("data.txt")[3] {
					0 => { win.printw("You continue deeper. A chest is sat against the wall.\n\n[OPEN]\n[BACK]"); }
					2 => { win.printw("There's that knife chest again.\n\n[OPEN]\n[BACK]"); }
					_ => { win.printw("You continue deeper, and stumble across another chest.\n\n[OPEN]\n[BACK]"); }
				}
				pos = 7;
			}
			1 => {
				win.printw("An empty chest lies in the darkness.\n\n[PUT BACK]\n[BACK    ]");
				pos = 11;
			}
			_ => { pos = 420 }
		}
		match table_seek(&win, 5, 6, pos) {
			5 => {}
			6|_ => {break}
		}
	}
}

fn cave_page(win: &pancurses::Window) {
	loop {
		win.mv(3, 0);
		win.printw("You make your way towards a deep, cavernous grotto.\nHardly a thing to make out through the dark.\n\n[CONTINUE]\n[ADMIRE  ]\n[GO LEFT ]\n[BACK    ]");
		match table_seek(&win, 6, 9, 11) {
			6 => {
				screen_smash(&win, 3, 9);
				cave_continue_page(&win);
			}
			7 => {
				let mut status = reader("data.txt")[2];
				if status <= 7 { status += 1; writer("data.txt", 2, status )}
				win.mv(11, 0);
				match status {
					2 => { win.printw("...a pretty dark one, at that."); }
					3 => { win.printw("Definitely a cave right here."); }
					4 => { win.printw("But is it, really?"); }
					5 => { win.printw("No one can ever truly know."); }
					6 => { win.printw("But one question remains..."); }
					7 => { win.printw("Why are you still doing this?"); }
					_ => { win.printw("Sure is a cave."); }
				}
				win.refresh();
				sleep(500);
				screen_smash(&win, 11, 11);
			}
			8 => {}
			9|_ => {break}
		}
	}
}

fn landing_site(win: &pancurses::Window) {
	loop {
		win.mv(3, 0);
		win.printw("You are Liam. An astronaut by trade, you took a bad\nturn on the Space Belt, and crash-landed on this strange,\nalien planet. You awaken, lain in a vast field of grass.\n\n[HILL]\n[CAVE]\n[SHIP]\n[QUIT]");
		match table_seek(&win, 7, 10, 7) {
			7 => {
				screen_smash(&win, 3, 10);
				hill_page(&win);
			}
			8 => {
				screen_smash(&win, 3, 10);
				cave_page(&win);
			}
			9 => {}
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
		match table_seek(&win, 5, 8, 11) {
			5 => {
				if ! exists("data.txt") { generate("data.txt", 20) }
				screen_smash(&win, 0, 11);
				display_header(&win);
				landing_site(&win);
				screen_smash(&win, 0, 11);
			}
			6 => {
				if exists("data.txt") {
					win.mv(10, 0);
					obo_blitter(&win, "Are you sure you want to reset?\n\n[YES]\n[NO ]", 10);
					match table_seek(&win, 12, 13, 6) {
						12 => {
							remove_file("data.txt").unwrap();
							generate("data.txt", 20);
							writer("data.txt", 1, 1);
							win.mv(15, 0);
							obo_blitter(&win, "Save reset.", 10);
							win.refresh();
							sleep(500);
							screen_smash(&win, 10, 15);
						}
						13|_ => {}
					}
					screen_smash(&win, 10, 13)
				}
			}
			7 => {
				win.mv(10, 0);
				obo_blitter(&win, "Copyright (c) 2021-22 draumaz.", 10);
				win.refresh();
				sleep(500);
				win.mv(11, 0);
				obo_blitter(&win, "All rights reserved.", 10);
				win.refresh();
				sleep(500);
				screen_smash(&win, 10, 11);
			}
			8|_ => {break}
		}
	}
}

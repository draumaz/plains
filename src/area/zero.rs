use crate::routine::{funk::{table_seek, screen_smash}, flourish::{display_header, obo_blitter}, misc::sleep};
use savesys::{exists, generate, reader, writer};

fn hill_river_page(win: &pancurses::Window) {
	let mode = reader("data.txt")[4];
	loop {
		win.mv(3, 0);
		win.printw("│ A river juts through the landscape.");
		win.mv(5, 0);
		match mode {
			1 => { win.printw("[RELAX]\n[FILL ]\n[BACK ]"); }
			3 => { win.printw("[RELAX]\n[EMPTY]\n[BACK ]"); }
			2|_ => { win.printw("[RELAX]\n[CHILL]\n[BACK ]"); }
		}
		match table_seek(&win, 5, 7, 8) {
			5 => {
				for i in ["You sit down a spell and take in the nature.", "How calming!"] { obo_blitter(&win, String::from(i), 9, 10, 1000) }
			}
			6 => {
				match mode {
					1 => {}
					3 => {}
					2|_ => {
						obo_blitter(&win, String::from("This is basically the same thing as relaxing, right?"), 9, 10, 500);
					}
				}
			}
			7|99 => {screen_smash(&win, 3, 7); break}
			_ => {}
		}
	}
}

fn hill_mountain_page(win: &pancurses::Window) {
	loop {
		win.mv(3, 0);
		win.printw("│ A gentle wind flows through the sky.");
		win.mv(4, 0);
		match reader("data.txt")[4] {
			1 => {
				win.printw("│ Seems like your phone's got service.");
		    	win.mv(6, 0); win.printw("[CALL]\n[BACK]");
			}
			_ => {
				win.printw("│ Not much to see up here.");
				win.mv(6, 0); win.printw("[COLD]\n[BACK]");
			}
		}
		match table_seek(&win, 6, 7, 7) {
			6 => {
				match reader("data.txt")[4] {
					0 => {
						obo_blitter(&win, String::from("Indeed, it is quite cold here."), 9, 10, 500);
						screen_smash(&win, 9, 9);
					}
					_ => {}
				}
				continue;
			}
			7|99 => {screen_smash(&win, 3, 7); break}
			_ => {}
		}
	}
}

fn hill_page(win: &pancurses::Window) {
	loop {
		win.mv(3, 0);
		win.printw("│ You venture out towards a gargantuan hill.\n│ Beside it runs a stream of quickly-flowing water.\n\n[USE PHONE]\n[MOUNTAIN ]\n[TO RIVER ]\n[BACK     ]");
		match table_seek(&win, 6, 9, 12) {
			6 => {
				match reader("data.txt")[4] {
					0 => {
						obo_blitter(&win, String::from("Seems like you lost your phone in the crash."), 11, 10, 500);
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
			9|99 => {screen_smash(&win, 3, 9); break}
			_ => {}
		}
	}
}

fn cave_goleft_battle_page(win: &pancurses::Window) {
	let ph = 20; let eh = 50; let mut inc = 0;
	obo_blitter(&win, String::from("│ * LIAM   | HP: "), 3, 10, 0); win.printw(ph.to_string());
	obo_blitter(&win, String::from("│ * LIZARD | HP: "), 4, 10, 0); win.printw(eh.to_string());
	loop {
		obo_blitter(&win, String::from("[FIGHT]\n[TALK ]\n[LEAVE]"), 6, 10, 0);
		match table_seek(&win, 6, 8, 8) {
			6 => {
				match reader("data.txt")[0] {
					1 => {
						obo_blitter(&win, String::from("─> [FISTS]\n─> [KNIFE]\n─> [BACK ]"), 10, 10, 0);
						match table_seek(&win, 10, 12, 11) {
							10 => {}
							11 => {
								writer("data.txt", 3, 1);
								writer("data.txt", 7, 1);
								writer("data.txt", 8, 1);
								for i in (0..50).rev() {
									if i == 9 { win.mv(4, 18); win.printw(" "); }
									win.mv(4, 17);
									win.printw(i.to_string());
									win.refresh();
									sleep(25);
								}
								obo_blitter(&win, String::from("│ * LIZARD | HP: 0 "), 4, 10, 0);
								sleep(2000);
								obo_blitter(&win, String::from("Blood splatters over your suit."), 14, 10, 5000);
								display_header(&win);
								obo_blitter(&win, String::from("You take the bottle."), 14, 10, 2000);
								screen_smash(&win, 3, 15);
								break;
							}
							12|_ => {screen_smash(&win, 10, 12)}
						}
					}
					_ => {
						match inc {
							0 => {
								for i in ["You try to hit him.", "He barely flinches.", "Seems like you're bothering him, though."] { obo_blitter(&win, String::from(i), 10, 10, 500) }
							}
							6 => {
								for i in 7..9 { writer("data.txt", i, 2) }
								for i in ["The lizard man is sick of you.", "He disappears into the distance."] {
									obo_blitter(&win, String::from(i), 10, 10, 1000);
								}
								sleep(1000);
								writer("data.txt", 3, 1);
								display_header(&win);
								obo_blitter(&win, String::from("Hey, look; a bottle!"), 10, 10, 1000);
								
								break;
							}
							1|2|3|4|5|_ => {
								obo_blitter(&win, String::from("..."), 10, 10, 500);
							}
						}
					}
				}
				screen_smash(&win, 10, 11);
				inc += 1;
			}
			7 => {
				match reader("data.txt")[0] {
					1 => { 
						obo_blitter(&win, String::from("He's afraid of you."), 10, 30, 1000); 
					}
					_ => {
						obo_blitter(&win, String::from("He doesn't quite understand why\nyou want to check the chest so badly."), 10, 10, 500);
					}
				}
			}
			8|99 => {screen_smash(&win, 3, 9); break}
			_ => {}
		}
	}
}

fn cave_continue_page(win: &pancurses::Window) {
	let mut pos: i32;
	loop {
		win.mv(3, 0);
		match reader("data.txt")[0] { // knife
			0 => {
				match reader("data.txt")[3] { // also bottle
					0 => { win.printw("│ You continue deeper. A chest is sat against the wall."); }
					_ => { win.printw("│ You continue deeper, and stumble across another chest."); }
				}
				win.mv(5, 0); win.printw("[OPEN]\n[BACK]");
				pos = 7;
			}
			1 => {
				win.printw("│ An empty chest lies in the darkness.\n\n[PLACE]\n[BACK ]");
				pos = 8;
			}
			2 => { 
				win.printw("│ There's that chest again.");
				win.mv(5, 0); win.printw("[OPEN]\n[BACK]");
				pos = 7;
			}
			_ => { pos = 420; }
		}
		match table_seek(&win, 5, 6, pos) {
			5 => {
				match reader("data.txt")[0] {
					1 => {
						writer("data.txt", 0, 2);
						display_header(&win);
						obo_blitter(&win, String::from("You put the knife back."), 8, 10, 500);
					}
					_ => {
						writer("data.txt", 0, 1);
						display_header(&win);
						obo_blitter(&win, String::from("You take the knife."), 8, 10, 500);
					}
				}
				screen_smash(&win, 3, 8);
			}
			6|99 => {screen_smash(&win, 3, 6); break}
			_ => {}
		}
	}
}

fn cave_page(win: &pancurses::Window) {
	let mut length: i32;
	loop {
		let lizard_alive = reader("data.txt")[7];
		win.mv(3, 0);
		win.printw("│ You make your way towards a deep, cavernous grotto.\n│ Hardly a thing to make out through the dark.\n\n");
		match lizard_alive {
			1|2 => {win.printw("[CONTINUE]\n[ADMIRE  ]\n[BACK    ]"); length = 8;}
			0|_ => {win.printw("[CONTINUE]\n[ADMIRE  ]\n[GO LEFT ]\n[BACK    ]"); length = 9;}
		}
		match table_seek(&win, 6, length, 11) {
			6 => {
				screen_smash(&win, 3, 9);
				cave_continue_page(&win);
			}
			7 => {
				let txt: &'static str;
				let num: i32;
				let mut status = reader("data.txt")[2];
				match lizard_alive {
					1|2 => {num = 10}
					_ => {num = 11}
				}
				if status <= 7 { status += 1; writer("data.txt", 2, status )}
				win.mv(11, 0);
				match status {
					2 => { txt = "...a pretty dark one, at that."; }
					3 => { txt = "Definitely a cave right here."; }
					4 => { txt = "But is it, really?"; }
					5 => { txt = "No one can ever truly know."; }
					6 => { txt = "But one question remains..."; }
					7 => { txt = "Why are you still doing this?"; }
					_ => { txt = "Sure is a cave."; }
				}
				obo_blitter(&win, String::from(txt), num, 10, 500);
			}
			8 => {
				if reader("data.txt")[7] == 0 {
					screen_smash(&win, 3, 9);
					cave_goleft_battle_page(&win);
				} else { screen_smash(&win, 3, 9); break }
			}
			9|99 => {screen_smash(&win, 3, 9); break}
			_ => {}
		}
	}
}

fn landing_site(win: &pancurses::Window) {
	loop {
		win.mv(3, 0);
		win.printw("│ You are Liam. Your only memories are of crashing on this distant planet.\n│ You awaken, lain in a vast field of grass. Your back hurts.\n\n[HILL]\n[CAVE]\n[SHIP]\n[QUIT]");
		match table_seek(&win, 6, 9, 7) {
			6 => {
				screen_smash(&win, 3, 10);
				hill_page(&win);
			}
			7 => {
				screen_smash(&win, 3, 10);
				cave_page(&win);
			}
			9|99 => {screen_smash(&win, 0, 10); break}
			8|_ => {}
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
					obo_blitter(&win, String::from("Are you sure you want to reset?\n\n[YES]\n[NO ]"), 10, 10, 0);
					match table_seek(&win, 12, 13, 6) {
						12 => {
							//remove_file("data.txt").unwrap();
							//generate("data.txt", 20);
							writer("data.txt", 0, 0);
							writer("data.txt", 1, 1);
							for i in 2..8 { writer("data.txt", i, 0); }
							obo_blitter(&win, String::from("Save reset."), 15, 10, 500);
						}
						13|_ => {}
					}
					screen_smash(&win, 10, 13);
				}
			}
			7 => {
				obo_blitter(&win, String::from("Copyright (c) 2021-22 draumaz."), 10, 10, 500);
				obo_blitter(&win, String::from("All rights reserved."), 11, 10, 500);
			}
			8|99 => {break}
			_ => {}
		}
	}
}

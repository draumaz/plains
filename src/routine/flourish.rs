use super::misc::{PLAINS_VERSION, sleep};
use savesys::reader;

pub fn display_header(win: &pancurses::Window) {
	win.mv(1, 0); win.printw("The Plains v"); win.printw(PLAINS_VERSION);
	let sav = reader("data.txt");
	match sav[0] {
		1 => {
			win.printw(" · [");
			win.printw(reader("data.txt")[0].to_string());
			win.printw("x KNIFE]");
		}
		_ => {
			match sav[3] {
				0|1 => { win.mv(1, 16); win.printw("			   "); }
				_ => {win.mv(1, 29); win.printw("              "); }
			}
		}
	}
	match sav[3] {
		1 => {
			if sav[0] != 1 { win.mv(1, 16); } else { win.mv(1, 29); }
			win.printw(" · [");
			win.printw(reader("data.txt")[3].to_string());
			win.printw("x BOTTLE]");
		}
		_ => { win.mv(1, 29); win.printw("           "); }
	}
	win.mv(2, 0); win.printw("┌───────────────────>");
}

pub fn obo_blitter(win: &pancurses::Window, text: &str, pos: i32, stop: u64, pause: u64) {
	win.mv(pos, 0);
	for c in String::from(text).chars() { win.printw(c.to_string()); win.refresh(); sleep(stop); }
	if pause == 0 {return}
	sleep(pause);
	for i in (0..text.len() as i32).rev() {
		win.mv(pos, i);
		win.printw(" ");
		win.refresh();
		sleep(stop);
	}
}

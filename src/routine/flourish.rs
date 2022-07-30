use super::misc::{PLAINS_VERSION, sleep};
use savesys::reader;

pub fn display_header(win: &pancurses::Window) {
	win.mv(1, 0); win.printw("The Plains v"); win.printw(PLAINS_VERSION);
	match reader("data.txt")[0] {
		1 => {
			win.printw(" · [");
			win.printw(reader("data.txt")[0].to_string());
			win.printw("x KNIFE]");
		}
		_ => { win.printw("           "); }
	}
	match reader("data.txt")[3] {
		1 => {
			win.printw(" · [");
			win.printw(reader("data.txt")[3].to_string());
			win.printw("x BOTTLE]");
		}
		_ => { win.printw("           "); }
	}
	win.mv(2, 0); win.printw("┌───────────────────>");
}

pub fn obo_blitter(win: &pancurses::Window, text: &'static str, stop: u64) {
	for c in text.chars() {
		win.printw(c.to_string());
		win.refresh();
		sleep(stop);
	}
}

pub fn obo_wiper(win: &pancurses::Window, y: i32, start: i32, stop: u64) {
	for i in (0..start).rev() {
		win.mv(y, i);
		win.printw(" ");
		win.refresh();
		sleep(stop);
	}
}

pub fn msw_blitter(win: &pancurses::Window, text: &'static str, pos: i32, stop: u64, obo: bool) {
	win.mv(pos, 0);
	if obo { obo_blitter(&win, text, stop) } else { win.printw(text); }
	win.refresh();
	sleep(stop);
}
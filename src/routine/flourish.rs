use super::misc::{PLAINS_VERSION, sleep};

pub fn display_header(win: &pancurses::Window) {
	win.mv(1, 0); win.printw("The Plains v"); win.printw(PLAINS_VERSION);
}

pub fn obo_blitter(win: &pancurses::Window, text: &'static str, stop: u64) {
	for c in text.chars() {
		win.printw(c.to_string());
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
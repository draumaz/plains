use crate::b_display::universal_tabler;
use crate::f_display::display_header;

fn landing_site_text(win: &pancurses::Window) {
	win.mv(3, 0);
	win.printw("You are Liam. An astronaut by trade, you took a bad\nturn on the Space Belt, and crash-landed on this strange,\nalien planet. You awaken, lain in a vast field of grass.\n\n[HILL]\n[CAVE]\n[SHIP]\n[QUIT]");
}

pub fn landing_site(win: &pancurses::Window) {
	display_header(&win);
	landing_site_text(&win);
	loop { match universal_tabler(&win, 7, 10, 8, 7) {
		7|8|9 => {continue}
		10|_ => {break}
	} }
}
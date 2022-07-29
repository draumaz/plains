use pancurses::{Input, resize_term, echo, noecho, curs_set};

pub fn universal_tabler(win: &pancurses::Window, first: i32, last: i32, x: i32) -> i32 {
	let mut y = first;
	loop {
		win.mv(y, x);
		win.printw("<");
		match win.getch() {
			Some(Input::KeyUp) | 
			Some(Input::Character('w')) |
			Some(Input::Character('i')) => {
				win.mv(y, x);
				win.printw("\n");
				if y == first { y = last } else { y -= 1 }
			},
			Some(Input::KeyDown) |
			Some(Input::Character('s')) |
			Some(Input::Character('k')) => {
				win.mv(y, x);
				win.printw("\n");
				if y == last { y = first } else { y += 1 }
			},
			Some(Input::Character('\n')) => { 
				win.mv(y, x);
				win.printw("\n");
				return y;
			},
			Some(_) => (),
			None => ()
		}
	} 
}

pub fn screen_smash(win: &pancurses::Window, min: i32, max: i32) {
	for i in min..max+1 {
		win.mv(i, 0);
		win.printw("\n");
		win.refresh();
	}
}

pub fn screen_up(s: &pancurses::Window) {
	s.keypad(true);
	resize_term(25, 80);
	curs_set(0);
	noecho();
}

pub fn screen_down() {
	curs_set(1);
	echo();
}

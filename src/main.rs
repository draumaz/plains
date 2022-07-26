extern crate pancurses;

mod b_display;

use b_display::{universal_tabler, screen_up, screen_down};
use pancurses::{initscr, endwin};

fn splash(win: &pancurses::Window) {
    win.mv(1, 0);
    win.printw("==THE PLAINS===============\n==DRAUMAZ, 2021-22=========\n==WRITTEN IN RUST!=========");
    win.mv(5, 0);
    win.printw("[PLAY   ]\n[RESET  ]\n[LICENSE]\n[QUIT   ]");
    loop { match universal_tabler(&win, 5, 8, 11, 5) {
        5|6|7 => {continue}
        8|_ => {break}
    } }
}

fn main() {
    let screen = initscr();
    screen_up(&screen);
    splash(&screen);
    screen_down();
    endwin();
}

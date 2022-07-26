mod b_display;
mod misc;

use misc::sleep;
use b_display::{universal_tabler, screen_up, screen_down, screen_smash};

use pancurses::{initscr, endwin};

fn splash(win: &pancurses::Window) {
    win.mv(1, 0);
    win.printw("==THE PLAINS===============\n==DRAUMAZ, 2021-22=========\n==WRITTEN IN RUST!=========");
    win.mv(5, 0);
    win.printw("[PLAY   ]\n[RESET  ]\n[LICENSE]\n[QUIT   ]");
    loop { match universal_tabler(&win, 5, 8, 11, 5) {
        5|6 => {continue}
        7 => {
            win.mv(10, 0);
            win.printw("Copyright 2021-22 draumaz.\nAll rights reserved.");
            win.refresh();
            sleep(1000);
            screen_smash(&win, 10, 11);
        }
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

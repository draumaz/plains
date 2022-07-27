mod routine;
mod misc;
mod area;

use misc::sleep;
use crate::routine::funk::{universal_tabler, screen_up, screen_down, screen_smash};

use crate::area::zero::landing_site;

use pancurses::{initscr, endwin};

fn splash_text(win: &pancurses::Window) {
    win.mv(1, 0);
    win.printw("==THE PLAINS===============\n==DRAUMAZ, 2021-22=========\n==WRITTEN IN RUST!=========");
    win.mv(5, 0);
    win.printw("[PLAY   ]\n[RESET  ]\n[LICENSE]\n[QUIT   ]");
}

fn splash(win: &pancurses::Window) {
    splash_text(&win);
    loop { match universal_tabler(&win, 5, 8, 11, 5) {
        5 => {
            screen_smash(&win, 0, 11);
            landing_site(&win);
            screen_smash(&win, 0, 11);
            splash_text(&win);
            continue;
        }
        6 => {continue}
        7 => {
            win.mv(10, 0);
            win.printw("Copyright 2021-22 draumaz.\nAll rights reserved.");
            win.refresh();
            sleep(1000);
            screen_smash(&win, 10, 11);
            continue
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

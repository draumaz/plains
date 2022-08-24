use crate::{
    routine::funk::{screen_up, screen_down},
    area::zero::splash_screen
};

use pancurses::{initscr, endwin};

mod routine;
mod prompts;
mod area;

fn main() {
    let screen = initscr();
    screen_up(&screen);
    splash_screen(&screen);
    screen_down();
    endwin();
}

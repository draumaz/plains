mod routine;
mod prompts;
mod area;

use crate::routine::funk::{screen_up, screen_down};
use crate::area::zero::splash_screen;

use pancurses::{initscr, endwin};

fn main() {
    let screen = initscr();
    screen_up(&screen);
    splash_screen(&screen);
    screen_down();
    endwin();
}

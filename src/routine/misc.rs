use std::{thread::{spawn, sleep as sl}, time::Duration};

pub static PLAINS_VERSION: &'static str = "0.26";

pub fn sleep(time: u64) {
	spawn(move||{sl(Duration::from_millis(time))}).join().unwrap();
}

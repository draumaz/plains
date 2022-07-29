use std::{thread::{spawn, sleep as sl}, time::Duration};

pub fn sleep(time: u64) {
	spawn(move||{sl(Duration::from_millis(time))}).join().unwrap();
}

use std::{thread, time};

pub fn sleep(time: u64) {
	thread::spawn(
		move || {
			thread::sleep(time::Duration::from_millis(time));
		}
	).join().unwrap();
}
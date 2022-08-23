pub fn hill_river(i: &str) -> &str { match i {
	"head" =>  { "| A river juts through the landscape." }
	"sub1" =>  { "You sit down a spell and take in the nature." }
	"sub11" => { "How calming!" }
	"sub2" =>  { "This is basically the same thing as relaxing, right?" }
	_ => { "ERROR" }
} }

pub fn hill_mountain(i: &str) -> &str { match i {
	"head" =>          { "| A gentle wind flows through the sky." }
	"head_phone" =>    { "| Seems like your phone's got service here." }
	"head_no_phone" => { "| Not much to see up here." }
	"sub1" =>          { "Indeed, it's quite cold here." }
	_ => { "ERROR" }
} }

pub fn hill(i: &str) -> &str { match i {
	"head" => { "│ You venture out towards a gargantuan hill.\n│ Beside it runs a stream of quickly-flowing water." }
	"sub1" => { "Seems like you lost your phone in the crash." }
	_ => { "ERROR" }
} }

pub fn cave_battle(i: &str) -> &str { match i {
	_ => { "ERROR" }
} }

pub fn cave_continue(i: &str) -> &str { match i {
	"head_no_bottle" => { "│ You continue deeper. A chest is sat against the wall." }
	"head_bottle" =>    { "│ You continue deeper, and stumble across another chest." }
	"head_empty" =>     { "| An empty chest lies in the darkness." }
	"head_put_back" =>  { "| There's that chest again." }
	"sub_take" =>       { "You take the knife." }
	"sub_put_back" =>   { "You put the knife back." }
	_ => { "ERROR" }
} }

pub fn cave(i: &str) -> &str { match i {
	"head" => { "│ You make your way towards a deep, cavernous grotto.\n│ Hardly a thing to make out through the dark." }
	_ => { "ERROR" }
} }

pub fn landing(i: &str) -> &str { match i {
	"head" => { "│ You are Liam. Your only memories are of crashing on this distant planet.\n│ You awaken, lain in a vast field of grass. Your back hurts." }
	_ => { "ERROR" }
} }

pub fn splash(i: &str) -> &str { match i {
	"hello" => { "==THE PLAINS===============\n==DRAUMAZ, 2021-22=========\n==WRITTEN IN RUST!=========" }
	"reset_warn" => { "Are you sure you want to reset?" }
	"reset_succ" => { "Save reset." }
	"copyright0" => { "Copyright (c) 2021-22 draumaz." }
	"copyright1" => { "All rights reserved." }
	_ => { "ERROR" }
} }
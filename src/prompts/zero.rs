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
	_ => { "ERROR" }
} }

pub fn cave_battle(i: &str) -> &str { match i { 
	_ => { "ERROR" }
} }

pub fn cave_continue(i: &str) -> &str { match i { 
	_ => { "ERROR" }
} }

pub fn cave(i: &str) -> &str { match i { 
	_ => { "ERROR" }
} }

pub fn landing(i: &str) -> &str { match i { 
	_ => { "ERROR" }
} }

pub fn splash(i: &str) -> &str { match i { 
	_ => { "ERROR" }
} }
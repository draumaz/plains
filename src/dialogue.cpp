#include <iostream>

int m1_dialogue(int p){
	if ( p == 1 ){
		std::cout << "You are Liam. An astronaut by trade, you took a bad turn on the Space Belt" << "\n" << "and landed on a strange planet. You awaken, laying in a field of grass." << "\n" << "You see hills, a cave, and strange flora." << std::endl;
	}
	if ( p == 11 ){
		std::cout << "You're covered in the blood of the innocent. The sky rumbles before you." << std::endl;
	}
	return 0;
}

int embark_dialogue(int p){
	if ( p == 1 ){
		std::cout << "You decide to depart anyways, and your journey comes to an end." << std::endl;
		return 0;
	}
	if ( p == 2 ){
		std::cout << "Saan mentions how beautiful this planet is." << std::endl;
		return 0;
	}
	if ( p == 21 ){
		std::cout << "Seems like they all want to stick around for a bit." << std::endl;
		return 0;
	}
	if ( p == 22 ){
		std::cout << "You and your friends disembark." << std::endl;
		return 0;
	}
	if ( p == 3 ){
		std::cout << "Blood still dripping from your clothes, you lock the doors and take off, leaving your friends behind." << std::endl;
		return 0;
	}
	if ( p == 31 ){
		std::cout << "Ignoring your friends, you make your way to their spaceship and lock the doors." << std::endl;
		return 0;
	}
	if ( p = 32 ){
		std::cout << "Your friends follow along." << std::endl;
		return 0;
	}
	if ( p = 33 ){
		std::cout <<  "This ship is gorgeous. Complex, shiny white metal covers the interior." << std::endl;
		return 0;
	}
	if ( p = 34 ){
		std::cout << "The ship doesn't matter, it's a means to an end." << std::endl;
		return 0;
	}
	if ( p = 35 ){
		std::cout << "You decide against leaving quite yet." << std::endl;
		return 0;
	}
	return 0;
}

int cave_dialogue(int p){
	if ( p == 1 ){
		std::cout << "You make your way towards a deep, dark cave. You can barely see anything." << std::endl;
		return 0;
	}
	if ( p == 2 ){
		std::cout << "Seems pretty forboding...best to head back." << std::endl;
		return 0;
	}
	if ( p == 3 ){
		std::cout << "You continue deeper down the cave. There's small box by the wall." << std::endl;
		return 0;
	}
	if ( p == 31 ){
		std::cout << "Just a dingy old cave." << std::endl;
		return 0;
	}
	if ( p == 32 ){
		std::cout << "You're deep into the cave. There's that box." << std::endl;
		return 0;
	}
	if ( p == 33 ){
		std::cout << "You open the box and find a knife. You put it in your pocket." << std::endl;
		return 0;
	}
	if ( p == 34 ){
		std::cout << "You open the box and put the knife back." << std::endl;
		return 0;
	}
	if ( p == 35 ){
		std::cout << "You take the knife back." << std::endl;
		return 0;
	}
	if ( p == 36 ){
		std::cout << "Continuing down a cave like this is just asking for trouble." << std::endl;
		return 0;
	}
	if ( p == 4 ){
		std::cout << "Up against the entrance is a sign. It's written in a system you don't recognize." << std::endl;
		return 0;
	}
	if ( p == 41 ){
		std::cout << "You pull out your phone, and attempt to translate the symbols." << std::endl;
		return 0;
	}
	if ( p == 411 ){
		std::cout << "...how rude." << std::endl;
		return 0;
	}
	if ( p == 412 ){
		std::cout << "Too much work, anyways." << std::endl;
		return 0;
	}
	if ( p = 5 ){
		std::cout << "You come across another unlocked chest. It's rather dusty." << std::endl;
		return 0;
	}
	if ( p == 51 ){
		std::cout << "There's that chest where you got the bottle." << std::endl;
		return 0;
	}
	if ( p == 52 ){
		std::cout << "There's that chest with the bottle." << std::endl;
		return 0;
	}
	if ( p == 511 ){
		std::cout << "You open the best and find an empty bottle." << std::endl;
		return 0;
	}
	if ( p == 512 ){
		std::cout << "You put the bottle back." << std::endl;
		return 0;
	}
	if ( p == 513 ){
		std::cout << "You take the bottle back." << std::endl;
		return 0;
	}
	return 0;
}

int hill_dialogue(int p){
	if ( p == 1 ){
		std::cout << "That hill looks pretty strange...it juts out of the landscape in an unnatural way." << std::endl;
		return 0;
	}
	if ( p == 11 ){
		std::cout << "You hear a strange noise. Perhaps heading back to your ship will reveal the source." << std::endl;
		return 0;
	}
	if ( p == 12 ){
		std::cout << "In the distance, you can see a creature moving about." << std::endl;
		return 0;
	}
	if ( p == 121 ){
		std::cout << "You can see the lizard sitting down, enjoying the sun." << std::endl;
		return 0;
	}
	if ( p == 2 ){
		std::cout << "The reptilian man seems untrusting of you, and leaves the area." << std::endl;
		return 0;
	}
	if ( p == 21 ){
		std::cout << "The reptilian man comes to you, and gives you some information." << std::endl;
		return 0;
	}
	if ( p == 211 ){
		std::cout << "You're far from home, aren't'cha?" << std::endl;
		return 0;
	}
	if ( p == 212 ){
		std::cout << "...not really helpful. But he means well." << std::endl;
		return 0;
	}
	if ( p == 22 ){
		std::cout << "The reptilian tells you that everyone seems to be scared of him except for you." << std::endl;
		return 0;
	}
	if ( p == 221 ){
		std::cout << "He looks really happy." << std::endl;
		return 0;
	}
	if ( p == 23 ){
		std::cout << "The huge reptilian sees you, and approaches." << std::endl;
		return 0;
	}
	if ( p == 231 ){
		std::cout << "The reptilian waves and smiles at you." << std::endl;
		return 0;
	}
	if ( p == 232 ){
		std::cout << "Looks like he's having a sense of déjà vu." << std::endl;
		return 0;
	}
	if ( p == 233 ){
		std::cout << "You give the lizard man the flower. He smiles at you." << std::endl;
	}
	if ( p == 234 ){
		std::cout << "I don't have the heart to program this. Sorry!" << std::endl;
		return 0;
	}
	if ( p == 235 ){
		 std::cout << "He tells you nobody's shown him kindness like this before." << std::endl;
		 return 0;
	}
	if ( p == 236 ){
		std::cout << "Upon seeing the towering lizard, you decide to head back." << std::endl;
		return 0;
	}
	if ( p == 3 ){
		std::cout << "Silence fills the air." << std::endl;
		return 0;
	}
	if ( p == 31 ){
		std::cout << "You lay the flower down next to his lifeless corpse." << std::endl;
		return 0;
	}
	if ( p == 311 ){
		std::cout << "You use the bottle to collect his blood. Still warm." << std::endl;
		return 0;
	}
	if ( p == 4 ){
		std::cout << "You're completely motionless." << std::endl;
	}
	if ( p == 41 ){
		std::cout << "Suddenly, you hear a sound coming from near your ship." << std::endl;
		return 0;
	}
	if ( p == 412 ){
		std::cout << "You hear a whirring sound by your crashsite." << std::endl;
		return 0;
	}
	if ( p == 5 ){
		std::cout << "Despite all that lies ahead, you decide to simply stand still." << std::endl;
		return 0;
	}
	if ( p == 51 ){
		std::cout << "Seems like a waste of time." << std::endl;
		return 0;
	}
	if ( p == 512 ){
		std::cout << "You decide to stop being motionless, and return to a life full of motion." << std::endl;
		return 0;
	}
	if ( p == 513 ){
		std::cout << "Stand still." << std::endl;
		return 0;
	}
	if ( p == 514 ){
		std::cout << "Go back." << std::endl;
		return 0;
	}
	if ( p == 6 ){
		std::cout << "You sit down on the soft grass and take in your surroundings.\nYou see a flower growing." << std::endl;
		return 0;
	}
	if ( p == 61 ){
		std::cout << "The flower comes off its root without hesitation." << std::endl;
		return 0;
	}
	if ( p == 611 ){
		std::cout << "You put it in your pocket." << std::endl;
		return 0;
	}
	if ( p == 62 ){
		std::cout << "You lay down for a moment, and feel refreshed." << std::endl;
		return 0;
	}
	if ( p == 621 ){
		std::cout << "You decide that there's more important things to be doing." << std::endl;
		return 0;
	}
	return 0;
}

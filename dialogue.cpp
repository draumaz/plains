#include <iostream>

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

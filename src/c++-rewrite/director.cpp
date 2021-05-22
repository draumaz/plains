#include <iostream>
#include "visuals.hpp"

int direct(){
	int i;
	screen_clear();
	std::cout << "\n";
	splash_display();
	std::cout << "\n" << "PLAY [1]" << "\nRESET [2]" << "\n\nACTION >> ";
	std::cin >> i;
	if (i == 1){
		std::cout << "game direct" << std::endl;
		return 0;
	}
	if (i == 2){
		std::cout << "reset direct" << std::endl;
		return 0;
	}
	else{
		std::cout << "FUCK" << std::endl;
		return 0;
	}
	//
	return 0;
}

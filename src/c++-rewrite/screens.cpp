#include <iostream>
#include <fstream>
#include <string>
#include "backend.hpp"
#include "dialogue.hpp"
#include "visuals.hpp"

using namespace std;

void cave_main_screen(){
	screen_clear();
	version_header();
	int p,i;
	p = 1;
	cave_dialogue(p);
	cout << "\n" << "GO FORWARDS [1]" << "\n" << "LOOK AROUND [2]" << "\n" << "GO RIGHT [3]" << "\n" << "BACK [4]" << "\n\n" << "ACTION >> ";
	cin >> i;
}


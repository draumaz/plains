#include <iostream>
#include <fstream>
#include <string>
#include <unistd.h>
#include <time.h>
#include "backend.hpp"
#include "dialogue.hpp"
#include "visuals.hpp"
#include "screens.hpp"

using namespace std;

void m1_main_screen(){
	screen_clear();
	version_header();
	inventory_display();
	int p,i;
	p = 1;
	m1_dialogue(p);
	cout << "\n" << "HILL [1]" << "\n" << "CAVE [2]" << "\n" << "TOOL [3]" << "\n" << "QUIT [4]" << "\n\n" << "ACTION >> ";
	cin >> i;
	if ( i == 2 ){
		cave_main_screen();
	}
	if ( i == 4 ){
		screen_clear();
		exit(0);
	}
}

void cave_deeper_screen(){
	screen_clear();
	version_header();
	inventory_display();
	int * x = save_reader();
	int v15 = x[14];
	int p,i;
	string k;
	if ( v15 == 0 ){
		p = 3;
		k = "OPEN";
	}
	if ( v15 == 1 ){
		p = 31;
		k = "PUT BACK";
	}
	if ( v15 == 2 ){
		p = 32;
		k = "TAKE BACK";
	}
	cave_dialogue(p);
	cout << "\n" << k << " [1]" << "\n" << "BACK [2]" << "\n\n" << "ACTION >> ";
	cin >> i;
	if ( i == 2 ){
		cout << "" << endl;
		p = 36;
		cave_dialogue(p);
		sleep(2);
		cave_main_screen();
	}
}

void cave_main_screen(){
	screen_clear();
	version_header();
	inventory_display();
	int p,i;
	p = 1;
	cave_dialogue(p);
	cout << "\n" << "GO FORWARDS [1]" << "\n" << "LOOK AROUND [2]" << "\n" << "GO RIGHT [3]" << "\n" << "BACK [4]" << "\n\n" << "ACTION >> ";
	cin >> i;
	if ( i == 1 ){
		cave_deeper_screen();
	}
	if ( i == 4 ){
		p = 2;
		cout << "" << endl;
		cave_dialogue(p);
		sleep(2);
		m1_main_screen();
	}
}


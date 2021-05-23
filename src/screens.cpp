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
	if ( i == 1 ){
		hill_main_screen();
	}
	if ( i == 2 ){
		cave_main_screen();
	}
	if ( i == 4 ){
		screen_clear();
		exit(0);
	}
}

void hill_evil_stand_screen(){
	screen_clear();
	version_header();
	inventory_display();
	int p,i;
	p = 513;
	cout << "" << endl;
	hill_dialogue(p);
	cout << "\n" << "   [1]" << "\n" << "STAND STILL [2]" << "\n" << "    [3]" << "\n\n" << "ACTION >> ";
	cin >> i;
	if ( i == 1 ){
		hill_evil_stand_screen();
	}
	if ( i == 2 ){
		//
	}
	if ( i == 3 ){
		hill_evil_stand_screen();
	}
}

void hill_main_screen(){
	screen_clear();
	version_header();
	inventory_display();
	int * x = save_reader();
	int v1 = x[0];
	int v6 = x[5];
	int v12 = x[11];
	int v16 = x[15];
	int p,i;
	string s1;
	string s2;
	if ( v6 == 1 and v1 == 0 ){
		hill_evil_stand_screen();
	}
	if ( v6 == 0 and v12 == 0 and v16 != 2 ){
		s1 = "GO TOWARDS THE CREATURE";
		p = 1;
		hill_dialogue(p);
		p = 12;
		hill_dialogue(p);
	}
	if ( v16 == 2 ){
		p = 121;
		s1 = "VISIT";
		hill_dialogue(p);
	}
	if ( v6 == 0 and v1 == 1 ){
		p = 11;
		hill_dialogue(p);
	}
	if ( v6 == 1 and v1 == 1 ){
		p = 514;
		hill_dialogue(p);
	}
	if ( v6 == 1 ){
		s1 = "GO FORWARDS";
	}
	if ( v1 == 0 ){
		s2 = "STAND STILL";
	}
	cout << "\n" << s1 << " [1]" << "\n" << s2 << " [2]" << "\n" << "TAKE A BREAK [3]" << "\n" << "BACK [4]" << "\n\n" << "ACTION >> ";
	cin >> i;
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


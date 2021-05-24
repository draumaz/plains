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
	cout << "\n" << "HILL [1]" << "\n" << "CAVE [2]" << "\n" << "TOOL [3]" << "\n" << "QUIT [4]" << endl;
	i = input_display();
	if ( i == 1 ){
		hill_main_screen();
	}
	if ( i == 2 ){
		cave_main_screen();
	}
	if ( i == 3 ){
		// Tool
	}
	if ( i == 4 ){
		screen_clear();
		exit(0);
	}
	if ( i != 1 or i != 2 or i != 3 or i != 4 ){
		error_handle();
		m1_main_screen();
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
	cout << "\n" << "            [1]" << "\n" << "STAND STILL [2]" << "\n" << "            [3]" << endl;
	i = input_display();
	if ( i == 1 ){
		hill_evil_stand_screen();
	}
	if ( i == 2 ){
		hill_stand_screen();
	}
	if ( i == 3 ){
		hill_evil_stand_screen();
	}
	if ( i != 1 or i != 2 or i != 3 ){
		error_handle();
		hill_evil_stand_screen();
	}
}

void hill_stand_screen(){
	screen_clear();
	version_header();
	inventory_display();
	int * x = save_reader();
	int p,i,line,state;
	int v6 = x[5];
	if ( v6 == 0 ){
		p = 5;
		hill_dialogue(p);
	}
	sleep(2);
	cout << "..." << endl;
	line = 0;
	state = 1;
	save_writer(line, state);
	sleep(2);
	if ( v6 == 0 ){
		p = 4;
		hill_dialogue(p);
		sleep(2);
		p = 41;
		cout << endl;
		hill_dialogue(p);
		sleep(2);
		hill_main_screen();
	}
	if ( v6 == 1 ){
		p = 412;
		cout << endl;
		hill_dialogue(p);
		sleep(2);
		hill_main_screen();
	}
}

void hill_lizard_dead_screen(){
	screen_clear();
	version_header();
	inventory_display();
	int * x = save_reader();
	int p,i,line,state;
	string a,b;
	int v5 = x[4];
	int v6 = x[5];
	int v16 = x[15];
	int v17 = x[16];
	p = 3;
	if ( v16 == 1 ){
		a = "PLACE FLOWER";
	}
	if ( v17 == 1 ){
		b = "COLLECT BLOOD";
	}
	hill_dialogue(p);
	cout << a << " [1]\n" << b << "[2]\nBACK [3]" << endl;
	i = input_display();
	if ( i == 1 ){
		if ( v16 == 1 ){
			line = 15;
			state = 4;
			p = 31;
			save_writer(line, state);
			cout << endl;
			hill_dialogue(p);
			sleep(3);
			hill_lizard_dead_screen();
		}
		if ( v16 != 1 ){
			hill_lizard_dead_screen();
		}
	}
	if ( i == 2 ){
		if ( v17 == 1 ){
			line = 16;
			state = 3;
			p = 311;
			save_writer(line, state);
			cout << endl;
			hill_dialogue(p);
			sleep(3);
			hill_lizard_dead_screen();
		}
		if ( v17 != 1 ){
			hill_lizard_dead_screen();
		}
	}
	if ( i == 3 ){
		hill_main_screen();
	}
	if ( i != 1 or i != 2 or i != 3 ){
		error_handle();
		hill_lizard_dead_screen();
	}
}

void hill_lizard_neutral_screen(){
	screen_clear();
	version_header();
	inventory_display();
	int * x = save_reader();
	int v7 = x[6];
	int v15 = x[14];
	int v16 = x[15];
	int p,i,line,state;
	if ( v16 != 2 ){
		p = 23;
	}
	if ( v16 == 2 ){
		p = 231;
	}
	if ( v7 == 1 ){
		p = 232;
	}
	hill_dialogue(p);
	if ( v15 == 1 ){
		cout << "\nFIGHT [1]" << endl;
	}
	else {
		cout << endl;
	}
	cout << "TALK [2]" << endl;
	if ( v16 == 0 or v16 == 2 ){
		cout << "BACK [3]" << endl;
	}
	if ( v16 == 1 ){
		cout << "GIVE FLOWER [3]\nBACK [4]" << endl;
	}
	i = input_display();
	if ( i == 1 ){
		if ( v16 == 2 and v15 == 1 ){
			p = 234;
			cout << endl;
			hill_dialogue(p);
			sleep(3);
			hill_lizard_neutral_screen();
		}
		if ( v15 == 1 ){
			// Battle
		}
		if ( v15 == 0 ){
			error_handle();
			hill_lizard_neutral_screen();
		}
	}
	if ( i == 2 ){
		if ( v7 == 0 and v16 == 2 ){
			p = 22;
			cout << endl;
			hill_dialogue(p);
			sleep(2);
			p = 221;
			hill_dialogue(p);
			sleep(3);
			hill_main_screen();
		}
		if ( v7 == 1 ){
			line = 11;
			state = 1;
			save_writer(line, state);
			p = 2;
			cout << endl;
			hill_dialogue(p);
			sleep(3);
			hill_main_screen();
		}
		if ( v7 == 0 ){
			p = 21;
			cout << endl;
			hill_dialogue(p);
			sleep(2);
			p = 211;
			hill_dialogue(p);
			sleep(2);
			cout << endl;
			p = 212;
			hill_dialogue(p);
			sleep(3);
			hill_lizard_neutral_screen();
		}
	}
	if ( i == 3 ){
		if ( v16 == 0 ){
			p = 236;
			cout << endl;
			hill_dialogue(p);
			sleep(2);
			hill_main_screen();
		}
		if ( v16 == 1 ){
			line = 15;
			state = 2;
			save_writer(line, state);
			p = 233;
			cout << endl;
			hill_dialogue(p);
			sleep(2);
			hill_lizard_neutral_screen();
		}
		if ( v16 == 2 ){
			p = 235;
			cout << endl;
			hill_dialogue(p);
			sleep(2);
			hill_main_screen();
		}
	}
	if ( i == 4 ){
		if ( v16 != 1 ){
			error_handle();
			hill_lizard_neutral_screen();
		}
		if ( v16 == 1 ){
			p = 236;
			cout << endl;
			hill_dialogue(p);
			sleep(2);
			hill_main_screen();
		}
	}
	if ( i != 1 or i != 2 or i != 3 or i != 4 ){
		error_handle();
		hill_lizard_neutral_screen();
	}
}

void hill_break_screen(){
	screen_clear();
	version_header();
	inventory_display();
	int * x = save_reader();
	int p,i,line,state;
	int v16 = x[15];
	string v;
	p = 6;
	hill_dialogue(p);
	if ( v16 == 0 ){
		p = 601;
		v = "PICK";
		hill_dialogue(p);
		
	}
	if ( v16 == 1 ){
		v = "INSPECT";
	}
	cout << "\n" << v << " [1]\nLAY DOWN [2]\nBACK [3]" << endl;
	i = input_display();
	if ( i == 1 ){
		if ( v16 == 0 ){
			line = 15;
			state = 1;
			save_writer(line, state);
			p = 61;
			cout << endl;
			hill_dialogue(p);
			sleep(2);
			p = 611;
			hill_dialogue(p);
			sleep(1);
			hill_break_screen();
		}
		if ( v16 == 1 ){
			p = 602;
			cout << endl;
			hill_dialogue(p);
			sleep(2);
			hill_break_screen();
		}
	}
	if ( i == 2 ){
		p = 62;
		cout << endl;
		hill_dialogue(p);
		sleep(2);
		hill_break_screen();
	}
	if ( i == 3 ){
		if ( v16 == 0 ){
			p = 621;
			cout << endl;
			hill_dialogue(p);
			sleep(2);
		}
		hill_main_screen();
	}
	if ( i != 1 or i != 2 or i != 3 ){
		error_handle();
		hill_break_screen();
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
		cout << endl;
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
		s2 = "STAND STILL [2]";
	}
	if ( v1 == 1 ){
		s2 == "";
	}
	cout << "\n" << s1 << " [1]" << "\n" << s2 << "\n" << "TAKE A BREAK [3]" << "\n" << "BACK [4]" << endl;
	i = input_display();
	if ( i == 1 ){
		if ( v6 == 1 ){
			hill_lizard_dead_screen();
		}
		if ( v6 == 0 and v12 == 0 ){
			hill_lizard_neutral_screen();
		}
	}
	if ( i == 2 ){
		if ( v1 == 0 ){
			hill_stand_screen();
		}
		if ( v1 == 1 ){
			error_handle();
			hill_main_screen();
		}
	}
	if ( i == 3 ){
		hill_break_screen();
	}
	if ( i == 4 ){
		m1_main_screen();
	}
	if ( i != 1 or i != 2 or i != 3 or i != 4 ){
		error_handle();
		hill_main_screen();
	}

}

void cave_right_screen(){
        screen_clear();
        version_header();
        inventory_display();
        int * x = save_reader();
        int p,i,line,state;
        int blade_state = x[14];
	int bottle_state = x[16];
	string v;
	if ( bottle_state == 0 ){
		p = 6;
	}
	if ( bottle_state == 1 ){
		p = 63;
	}
	if ( blade_state == 0 ){
		v = "";
	}
	if ( blade_state == 1 ){
		v = "SLASH [1]";
	}
	cave_dialogue(p);
	cout << "\n" << v << "\n" << "INSPECT [2]" << "\n" << "BACK [3]" << endl;
	i = input_display();
	if ( i == 1 ){
		if ( blade_state == 1 ){
			if ( bottle_state == 0 ){
				p = 61;
				cout << endl;
				cave_dialogue(p);
				line = 16;
				state = 1;
				save_writer(line, state);
				sleep(2);
				cave_right_screen();
			}
			if ( bottle_state == 1 ){
				p = 631;
				cout << endl;
				cave_dialogue(p);
				sleep(2);
				cave_right_screen();
			}
		}

	}
	if ( i == 2 ){
		if ( bottle_state == 0 ){
			p = 62;
			cout << endl;
			cave_dialogue(p);
			sleep(3);
			cave_right_screen();
		}
		if ( bottle_state == 1 ){
			p = 632;
			cout << endl;
			cave_dialogue(p);
			sleep(2);
			cave_right_screen();
		}
	}
	if ( i == 3 ){
		cave_main_screen();
	}
	if ( i != 1 or i != 2 or i != 3 ){
		error_handle();
		cave_right_screen();
	}
}

void cave_deeper_screen(){
	screen_clear();
	version_header();
	inventory_display();
	int * x = save_reader();
	int v15 = x[14];
	int p,i,line,state;
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
	cout << "\n" << k << " [1]" << "\n" << "BACK [2]" << endl;
	i = input_display();
	if ( i == 1 ){
		if ( v15 == 0 ){
			line = 14;
			state = 1;
			p = 33;
			save_writer(line, state);
			cout << endl;
			cave_dialogue(p);
			sleep(2);
			cave_deeper_screen();
		}
		if ( v15 == 1 ){
			line = 14;
			state = 2;
			p = 34;
			save_writer(line, state);
			cout << endl;
			cave_dialogue(p);
			sleep(2);
			cave_deeper_screen();
		}
		if ( v15 == 2 ){
			line = 14;
			state = 1;
			p = 35;
			save_writer(line, state);
			cout << endl;
			cave_dialogue(p);
			sleep(2);
			cave_deeper_screen();
		}
	}
	if ( i == 2 ){
		p = 36;
		cout << endl;
		cave_dialogue(p);
		sleep(2);
		cave_main_screen();
	}
	if ( i != 1 or i != 2 ){
		error_handle();
		cave_deeper_screen();

	}
}

void cave_main_screen(){
	screen_clear();
	version_header();
	inventory_display();
	int p,i;
	p = 1;
	cave_dialogue(p);
	cout << "\n" << "GO FORWARDS [1]" << "\n" << "LOOK AROUND [2]" << "\n" << "GO RIGHT [3]" << "\n" << "BACK [4]" << endl;
	i = input_display();
	if ( i == 1 ){
		cave_deeper_screen();
	}
	if ( i == 2 ){
		// Look around
	}
	if ( i == 3 ){
		cave_right_screen();
	}
	if ( i == 4 ){
		p = 2;
		cout << endl;
		cave_dialogue(p);
		sleep(2);
		m1_main_screen();
	}
	if ( i != 1 or i != 2 or i != 3 or i != 4 ){
		error_handle();
		cave_main_screen();
	}
}


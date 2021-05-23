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
	cout << "\n" << "   [1]" << "\n" << "STAND STILL [2]" << "\n" << "    [3]" << endl;
	i = input_display();
	if ( i == 1 ){
		hill_evil_stand_screen();
	}
	if ( i == 2 ){
		// Stand
	}
	if ( i == 3 ){
		hill_evil_stand_screen();
	}
	if ( i != 1 or i != 2 or i != 3 ){
		error_handle();
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
		s2 = "STAND STILL [2]";
	}
	if ( v1 == 1 ){
		s2 == "";
	}
	cout << "\n" << s1 << " [1]" << "\n" << s2 << "\n" << "TAKE A BREAK [3]" << "\n" << "BACK [4]" << endl;
	i = input_display();
	if ( i == 1 ){
		if ( v6 == 1 ){
			// Go forwards (dead)
		}
		if ( v16 == 2 ){
			// Visit (friendly)
		}
		if ( v6 == 0 and v12 == 0 and v16 != 2 ){
			// Go forwards (alive)
		}
	}
	if ( i == 2 ){
		if ( v1 == 0 ){
			// Stand
		}
		if ( v1 == 1 ){
			error_handle();
			hill_main_screen();
		}
	}
	if ( i == 3 ){
		// Take a Break
	}
	if ( i == 4 ){
		m1_main_screen();
	}
	if ( i != 1 or i != 2 or i != 3 or i != 4 ){
		error_handle();
		hill_main_screen();
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
		cout << "" << endl;
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
		// Go right (second chest)
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


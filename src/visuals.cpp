#include <iostream>
#include <string>
#include "backend.hpp"

using namespace std;

void splash_display(){
    cout << "==THE PLAINS======================" << endl;
    cout << "==MADE BY DRAUMAZ IN 2021=========" << endl;
    cout << "==WRITTEN IN C++!=================" << endl;
    cout << "==CHARACTER DESIGN BY BRYCE CANO==" << endl;
}

void screen_clear(){
	system("cls||clear");
}

void inventory_display(){
        int * i = save_reader();
        int murder_state = i[5];
        int blade_state = i[14];
        int flower_state = i[15];
        int bottle_state = i[16];
        int viz = 0;
        string flower;
        string bottle;
        string blade;
	string div = " | ";
        if ( blade_state != 0 or flower_state != 0 or bottle_state != 0 ){
                viz = 1;
        }
        if ( flower_state == 0 or flower_state == 2 or flower_state == 4 ){
                flower = "EMPTY";
        }
        if ( flower_state == 1 ){
                flower = "1x FLOWER";
        }
        if ( blade_state == 0 or blade_state == 2 ){
                blade = "EMPTY";
        }
        if ( blade_state == 1 and murder_state == 0 ){
                blade = "1x KNIFE";
        }
        if ( blade_state == 1 and murder_state == 1 ){
                blade = "1x KNIFE (BLOODIED)";
        }
        if ( bottle_state == 0 or bottle_state == 2 ){
                bottle = "EMPTY";
        }
        if ( bottle_state == 1 or bottle_state == 5 ){
                bottle = "1x BOTTLE (EMPTY)";
        }
        if ( bottle_state == 3 ){
                bottle = "1x BOTTLE (BLOOD)";
        }
        if ( bottle_state == 4 ){
                bottle = "1x BOTTLE (WATER)";
        }
        if ( viz == 1 ){
                cout << div << flower << div << blade << div << bottle << div << "\n" << endl;
        }
        if ( viz == 0 ){
		cout << "\n" << endl;
	}
}

void version_header(){
	string v = "0.26";
	cout << "\n" << "The Plains v" << v;
}

void header(){
	screen_clear();
	version_header();
	inventory_display();
}

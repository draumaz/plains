#include <iostream>
#include <fstream>
#include <unistd.h>
#include <time.h>
#include "backend.hpp"
#include "director.hpp"
#include "visuals.hpp"

using namespace std;

void std_reset(){
	ofstream x("data.txt");
	x<<"0\n0\n0\n0\n1\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0";
	x.close();
}

void resetter(){
	screen_clear();
	int * x = save_reader();
	int v9 = x[8];
	int i;
	if ( v9 == 0 ){
		cout << "\n" << "Doing this will reset everything. Are you sure?" << endl;
		cout << "\n" << "RESET [1]" << endl;
		cout << "BACK [2]" << endl;
	}
	if ( v9 == 1 ){
		cout << "\n" << "RESET [1]" << endl;
	}
	cout << "\nACTION >> ";
	cin >> i;
	if ( i ==  1 ){
		if ( v9 == 0 ){
			std_reset();
			cout << "\n" << "Reset." << endl;
			sleep(1);
			direct();
		}
		else{}
	}
}


	

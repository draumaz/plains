#include <iostream>
#include "visuals.hpp"
#include "backend.hpp"
#include "dialogue.hpp"
#include "screens.hpp"
#include "reset.hpp"

using namespace std;

int direct(){
	int i;
	int * x = save_reader();
	int s = x[1];
	screen_clear();
	cout << "\n";
	splash_display();
	cout << "\n" << "PLAY [1]" << "\nRESET [2]" << endl;
	i = input_display();
	if ( i == 1 ){
		if ( s == 0 ){
			m1_main_screen();
		}
		else {
			cout << "WIP" << endl;
			return 0;
		}
	}
	if ( i == 2 ){
		resetter();
		return 0;
	}
	if ( i != 1 or i != 2 ){
		error_handle();
		direct();
	}
	return 0;
}

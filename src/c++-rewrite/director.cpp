#include <iostream>
#include "visuals.hpp"
#include "backend.hpp"
#include "dialogue.hpp"

using namespace std;

int direct(){
	int i;
	screen_clear();
	cout << "\n";
	splash_display();
	cout << "\n" << "PLAY [1]" << "\nRESET [2]" << "\n\nACTION >> ";
	cin >> i;
	if (i == 1){
		cout << "game direct" << endl;
		return 0;
	}
	if (i == 2){
		cout << "reset direct" << endl;
		return 0;
	}
	if (i != 2 or i != 1){
		while(cin.fail()){
			input_error();
			direct();
		}
		input_error();
		direct();
	}
	return 0;
}

#include <iostream>
#include "visuals.hpp"

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
	else{
		cout << "FUCK" << endl;
		return 0;
	}
	return 0;
}

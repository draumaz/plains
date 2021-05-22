#include <iostream>
#include <string>

using namespace std;

void splash_display(){
    cout << "==THE PLAINS======================" << endl;
    cout << "==MADE BY DRAUMAZ IN 2021=========" << endl;
    cout << "==WRITTEN IN C++!=================" << endl;
    cout << "==CHARACTER DESIGN BY BRYCE CANO==" << endl;
}

void version_header(){
	string v = "0.26";
	cout << "The Plains v" << v << endl;
}

void screen_clear(){
	system("cls||clear");
}

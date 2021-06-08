#include <iostream>
#include <fstream>
#include <unistd.h>
#include <vector>
#include <time.h>

void error_handle(){
	std::cin.clear();
        std::cin.ignore(256,'\n');
        std::cout << "\n" << "Did you mean something else?" << std::endl;
        sleep(1);
}

int input_display(){
	int i;
	std::cout << "\nACTION >> ";
	std::cin >> i;
	while ( std::cin.fail() ){
		std::cin.clear();
		std::cin.ignore(256,'\n');
		std::cout << "\n" << "Did you mean something else?" << std::endl;
        	sleep(1);
		std::cout << "\nACTION >> ";
		std::cin >> i;
	}
	return i;
}

void save_gen(){
	std::ofstream i("data.txt");
	i << "0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n";
	i.close();
}

int * save_reader(){
	static int i[18];
	std::ifstream x("data.txt");
	x >> i[0] >> i[1] >> i[2] >> i[3] >> i[4] >> i[5] >> i[6] >> i[7] >> i[8] >> i[9] >> i[10] >> i[11] >> i[12] >> i[13] >> i[14] >> i[15] >> i[16] >> i[17];
	x.close();
	return i;
}

void save_writer(int line, int state){
	int * i = save_reader();
	i[line] = state;
	std::ofstream xy("data.txt");
	xy << i[0] << "\n" << i[1] << "\n" << i[2] << "\n" << i[3] << "\n" << i[4] << "\n" << i[5] << "\n" << i[6] << "\n" << i[7] << "\n" << i[8] << "\n" << i[9] << "\n" << i[10] << "\n" << i[11] << "\n" << i[12] << "\n" << i[13] << "\n" << i[14] << "\n" << i[15] << "\n" << i[16] << "\n" << i[17] << "\n";
	xy.close();
}

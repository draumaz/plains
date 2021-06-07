#include <iostream>
#include <fstream>
#include <unistd.h>
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
	static int ij[18];
	std::ifstream z("data.txt");
	z >> ij[0] >> ij[1] >> ij[2] >> ij[3] >> ij[4] >> ij[5] >> ij[6] >> ij[7] >> ij[8] >> ij[9] >> ij[10] >> ij[11] >> ij[12] >> ij[13] >> ij[14] >> ij[15] >> ij[16] >> ij[17];
	z.close();
	return ij;
}


void save_writer(int line, int state){
	static int v[18];
	std::ifstream xx("data.txt");
	xx >> v[0] >> v[1] >> v[2] >> v[3] >> v[4] >> v[5] >> v[6] >> v[7] >> v[8] >> v[9] >> v[10] >> v[11] >> v[12] >> v[13] >> v[14] >> v[15] >> v[16] >> v[17];
	v[line] = state;
	std::ofstream xy("data.txt");
	xy << v[0] << "\n" << v[1] << "\n" << v[2] << "\n" << v[3] << "\n" << v[4] << "\n" << v[5] << "\n" << v[6] << "\n" << v[7] << "\n" << v[8] << "\n" << v[9] << "\n" << v[10] << "\n" << v[11] << "\n" << v[12] << "\n" << v[13] << "\n" << v[14] << "\n" << v[15] << "\n" << v[16] << "\n" << v[17] << "\n";
}

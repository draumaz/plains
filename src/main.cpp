#include "director.hpp"
#include "backend.hpp"
#include <iostream>
#include <fstream>

int main(){
	std::ifstream i("data.txt");
	if(i){}
	else{
		save_gen();
	}
	i.close();
	direct();
}

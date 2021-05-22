#include <iostream>
#include <fstream>

void save_gen(){
	std::ofstream i("data.txt");
	i<<"0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n";
	i.close();
}

int * save_reader(){
	int a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r;
	static int ij[17];
	std::ifstream z("data.txt");
	z>>a>>b>>c>>d>>e>>f>>g>>h>>i>>j>>k>>l>>m>>n>>o>>p>>q>>r;
	ij[0] = a;
	ij[1] = b;
	ij[2] = c;
	ij[3] = d;
	ij[4] = e;
	ij[5] = f;
	ij[6] = g;
	ij[7] = h;
	ij[8] = i;
	ij[9] = j;
	ij[10] = k;
	ij[11] = l;
	ij[12] = m;
	ij[13] = n;
	ij[14] = o;
	ij[15] = p;
	ij[16] = q;
	ij[17] = r;
	z.close();
	return ij;
}


int save_writer(int line, int state){
	int a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r;
	std::ifstream xx("data.txt");
	xx>>a>>b>>c>>d>>e>>f>>g>>h>>i>>j>>k>>l>>m>>n>>o>>p>>q>>r;
	if ( line == 0 ){
		a = state;
	}
	if ( line == 1 ){
		b = state;
	}
	if ( line == 2 ){
		c = state;
	}
	if ( line == 3 ){
		d = state;
	}
	if ( line == 4 ){
		e = state;
	}
	if ( line == 5 ){
		f = state;
	}
	if ( line == 6 ){
		g = state;
	}
	if ( line == 7 ){
		h = state;
	}
	if ( line == 8 ){
		i = state;
	}
	if ( line == 9 ){
		j = state;
	}
	if ( line == 10 ){
		k = state;
	}
	if ( line == 11 ){
		l = state;
	}
	if ( line == 12 ){
		m = state;
	}
	if ( line == 13 ){
		n = state;
	}
	if ( line == 14 ){
		o = state;
	}
	if ( line == 15 ){
		p = state;
	}
	if ( line == 16 ){
		q = state;
	}
	if ( line == 17 ){
		r = state;
	}
	std::ofstream xy("data.txt");
	xy<<a<<"\n"<<b<<"\n"<<c<<"\n"<<d<<"\n"<<e<<"\n"<<f<<"\n"<<g<<"\n"<<h<<"\n"<<i<<"\n"<<j<<"\n"<<k<<"\n"<<l<<"\n"<<m<<"\n"<<o<<"\n"<<p<<"\n"<<q<<"\n"<<r<<"\n";
	return 0;
}


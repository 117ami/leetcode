
#include "aux.cpp"
#include "1253.reconstruct-a-2-row-binary-matrix.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	int u = 5, l=5; 
	vi cs = {2,1,2,0,1,0,1,2,0,1};
	
	u=4,l=7, cs = {2,1,2,2,1,1,1};
	vvi res = s.reconstructMatrix(u,l,cs);
	say(res);
	return 0;
}



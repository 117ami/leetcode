
#include "aux.cpp"
#include "924.minimize-malware-spread.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<vector<int>> g ={{1,1,1},{1,1,1},{1,1,1}};
	vector<int> i={1, 2};
	g = {{1,1,0,0,0,0,0,0,0,0},{1,1,0,0,0,0,0,0,0,1},{0,0,1,0,1,0,0,0,0,1},{0,0,0,1,0,0,0,0,0,1},{0,0,1,0,1,0,1,0,0,1},{0,0,0,0,0,1,1,0,0,0},{0,0,0,0,1,1,1,0,0,1},{0,0,0,0,0,0,0,1,1,0},{0,0,0,0,0,0,0,1,1,0},{0,1,1,1,1,0,1,0,0,1}};
		i = {9,0,2};
	say(s.minMalwareSpread(g, i));
	return 0;
}


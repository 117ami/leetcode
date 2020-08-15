
#include "aux.cpp"
#include "928.minimize-malware-spread-ii.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<vector<int>> g = {{1, 1, 0, 0}, {1, 1, 1, 0}, {0, 1, 1, 1}, {0, 0, 1, 1}};
	vector<int> is = {0, 1};
	g = {{1,1,0,0},{1,1,0,1},{0,0,1,0},{0,1,0,1}}; 
	g = {{1,0,0,0,0,0},{0,1,0,0,0,0},{0,0,1,0,0,0},{0,0,0,1,1,0},{0,0,0,1,1,0},{0,0,0,0,0,1}};
	is = {5,0};
	say(s.minMalwareSpread(g, is));
	return 0;
}


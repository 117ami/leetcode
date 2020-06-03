
#include "aux.cpp"
#include "1192.critical-connections-in-a-network.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<vector<int>> con = {{0, 1}, {1, 2}, {2, 0}, {1, 3}}; 
	vector<vector<int>> res = s.criticalConnections(4, con); 
	say(res);
	return 0;
}


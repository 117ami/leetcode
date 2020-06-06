
#include "aux.cpp"
#include "406.queue-reconstruction-by-height.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<vector<int>> p = {{5,0}, {4, 1}};
	vector<vector<int>> res = s.reconstructQueue(p);
	say(res);
	return 0;
}


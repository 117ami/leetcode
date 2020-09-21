
#include "aux.cpp"
#include "1591.strange-printer-ii.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	std::vector<vector<int>> targetGrid = {{1,1,1,1},{1,2,2,1},{1,2,2,1},{1,1,1,1}} ;
	targetGrid = {{1,1,1,1},{1,1,3,3},{1,1,3,4},{5,5,1,4}} ;
	// targetGrid = {{1,2,1},{2,1,2},{1,2,1}} ;
	// targetGrid = {{1,1,1},{3,1,3}} ;
	// targetGrid={{1}};
	say(s.isPrintable(targetGrid));
	return 0;
}



#include "aux.cpp"
#include "1557.minimum-number-of-vertices-to-reach-all-nodes.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
int n = 6 ;
std::vector<vector<int>> edges = {{0,1},{0,2},{2,5},{3,4},{4,2}} ;

// int n = 5 ;
// std::vector<vector<int>> edges = {{0,1},{2,1},{3,1},{1,4},{2,4}} ;
say(s.findSmallestSetOfVertices(n, edges));



	return 0;
}


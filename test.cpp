
#include "aux.cpp"
#include "1559.detect-cycles-in-2d-grid.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	// std::vector<vector<char>> grid = {{'a','a','a','a'},{'a','b','b','a'},{'a','b','b','a'},{'a','a','a','a'}} ;
	std::vector<vector<char>> grid = {{'c','c','c','a'},{'c','d','c','c'},{'c','c','e','c'},{'f','c','c','c'}} ;
	// std::vector<vector<char>> grid = {{'a','b','b'},{'b','z','b'},{'b','b','a'}} ;
	grid = {{'b', 'a', 'c'}, {'c', 'a', 'c'}, {'d','d', 'c'}, {'b','c', 'c'}};
	say(s.containsCycle(grid));
	return 0;
}


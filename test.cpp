
#include "aux.cpp"
#include "980.unique-paths-iii.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvi grid = {{1,0,0,0},{0,0,0,0},{0,0,0,2}};
	say(s.uniquePathsIII(grid));
	return 0;
}


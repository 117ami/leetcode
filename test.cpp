
#include "aux.cpp"
#include "959.regions-cut-by-slashes.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vs grid = {"/\\", "\\/"};
	say(s.regionsBySlashes(grid));
	return 0;
}



#include "aux.cpp"
#include "797.all-paths-from-source-to-target.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvi g = {{1,2},{3},{3},{}};
	vvi res = s.allPathsSourceTarget(g);
	say(res);
	return 0;
}


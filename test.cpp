
#include "aux.cpp"
#include "130.surrounded-regions.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvc b = {{'O', 'O'}};
	s.solve(b);
	say(b);
	return 0;
}


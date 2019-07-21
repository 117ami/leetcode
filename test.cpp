
#include "aux.cpp"
#include "1128.number-of-equivalent-domino-pairs.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvi ds = {{1, 2}, {2, 1}, {2, 1}, {2, 1}};
	say(s.numEquivDominoPairs(ds));
	return 0;
}


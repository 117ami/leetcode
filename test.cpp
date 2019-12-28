
#include "aux.cpp"
#include "115.distinct-subsequences.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string sa = "babgbag", t = "bag";
	say(s.numDistinct(sa, t));
	return 0;
}


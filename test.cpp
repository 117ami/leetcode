
#include "aux.cpp"
#include "893.groups-of-special-equivalent-strings.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vs a = {"abc","acb","bac","bca","cab","cba"};
	say(s.numSpecialEquivGroups(a));
	return 0;
}


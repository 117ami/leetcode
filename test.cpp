
#include "aux.cpp"
#include "1288.remove-covered-intervals.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvi is = {{34335,39239},{15875,91969},{29673,66453},{53548,69161},{40618,93111}};
	is = {{2, 8}, {4, 8}, {3, 6}};
	say(s.removeCoveredIntervals(is));
	return 0;
}


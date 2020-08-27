
#include "aux.cpp"
#include "436.find-right-interval.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvi ns= {{3,4},{2, 3}, {1,2}};
	ns = {{1,2},{2,3},{0,1},{3,4}};
	say(s.findRightInterval(ns));
	vi v = {0,1,2,3};
	auto it = lower_bound(v.begin(), v.end(), 2);
	say(it - v.begin());
	return 0;
}


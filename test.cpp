
#include "aux.cpp"
#include "5292.divide-array-in-sets-of-k-consecutive-numbers.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi ns {3,2,1,2,3,4,3,4,5,9,10,11};
	ns = {3,3,2,2,1,1};
	int k = 3; 
	say(s.isPossibleDivide(ns, k));
	return 0;
}



#include "aux.cpp"
#include "5454.least-number-of-unique-integers-after-k-removals.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<int> a = {1,1,1,2,2,3}; 
	say(s.findLeastNumOfUniqueInts(a, 2));
	return 0;
}


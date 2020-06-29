
#include "aux.cpp"
#include "1497.check-if-array-pairs-are-divisible-by-k.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi ns = {-1,1,-2,2,-3,3,-4,4};
	int k = 3; 
	say(s.canArrange(ns, k));
	return 0;
}


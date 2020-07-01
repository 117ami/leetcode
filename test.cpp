
#include "aux.cpp"
#include "1425.constrained-subsequence-sum.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi ns = {10,-2,-10,-5,20}; 
	say(s.constrainedSubsetSum(ns, 2));
	return 0;
}


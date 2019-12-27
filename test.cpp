
#include "aux.cpp"
#include "974.subarray-sums-divisible-by-k.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi a = {4,5,0,-2,-3,1}; int k = 5; 
	a = {7, 4, -10}; 
	say(s.subarraysDivByK(a, k));
	return 0;
}


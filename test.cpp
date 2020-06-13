
#include "aux.cpp"
#include "368.largest-divisible-subset.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<int> v = {1,3,9,18,90,180,360,720,540, 108};
	v={1};
	say(s.largestDivisibleSubset(v));
	return 0;
}


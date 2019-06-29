
#include "aux.cpp"
#include "718.maximum-length-of-repeated-subarray.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi a {1,2,3,2,1}, b{3,2,1,4,7};
	say(s.findLength(a, b));
	return 0;
}


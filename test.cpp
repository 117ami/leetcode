
#include "aux.cpp"
#include "1356.sort-integers-by-the-number-of-1-bits.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi arr = {1,2,3,4,5,6,7,8};
	arr = {1024,512,256,128,64,32,16,8,4,2,1};
	say(s.sortByBits(arr));
	return 0;
}


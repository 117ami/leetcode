
#include "aux.cpp"
#include "1342.reduce-array-size-to-the-half.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi v = {3,3,3,3,5,5,5,7,2,2};
	v = {1,2,3,4,5,6,7,8,9,10};
	say(s.minSetSize(v));
	return 0;
}


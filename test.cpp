
#include "aux.cpp"
#include "1187.make-array-strictly-increasing.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi a = {5,3,7,8}, b={3,4,5,6};
	say(s.makeArrayIncreasing(a,b));
	return 0;
}


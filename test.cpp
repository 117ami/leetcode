
#include "aux.cpp"
#include "349.intersection-of-two-arrays.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi a = {2,6,3, 4, 4,4, 9, 4,9}, b = {9, 9, 4, 5, 2, 0};
	say(s.intersection(a, b));
	return 0;
}


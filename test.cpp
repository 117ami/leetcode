
#include "aux.cpp"
#include "1122.relative-sort-array.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi a = {2,3,1,3,2,4,6,7,9,2,19}, b = {2,1,4,3,9,6};
	say(s.relativeSortArray(a, b));
	return 0;
}


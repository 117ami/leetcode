
#include "aux.cpp"
#include "1157.online-majority-element-in-subarray.cpp"

int main(int argc, char const *argv[]) {
	vi arr = {1,1,2,2,1,1};
	MajorityChecker s(arr);
	say(s.query(0, 5, 4));
	return 0;
}


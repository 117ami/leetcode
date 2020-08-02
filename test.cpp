
#include "aux.cpp"
#include "1482.minimum-number-of-days-to-make-m-bouquets.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi b = {1,10,2,9,3,8,4,7,5,6};
	say(s.minDays(b, 4, 2));
	return 0;
}



#include "aux.cpp"
#include "5318.minimum-number-of-taps-to-open-to-water-a-garden.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	int n = 5; 
	vi ranges = {3,4,1,1,0,0};
	say(s.minTaps(n, ranges));
	return 0;
}


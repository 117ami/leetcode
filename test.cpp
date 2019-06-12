
#include "aux.cpp"
#include "c.cpp"
#include "313.super-ugly-number.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi primes{2,7,13,19};
	primes = {7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251};
	say(s.nthSuperUglyNumber(100000, primes));
	return 0;
}


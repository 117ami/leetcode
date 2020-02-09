
#include "aux.cpp"
#include "1347.minimum-number-of-steps-to-make-two-strings-anagram.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string ss = "friend", t = "family";
	say(s.minSteps(ss, t));
	return 0;
}


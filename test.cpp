
#include "aux.cpp"
#include "686.repeated-string-match.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string sa = "abcd", sb = "cdabcdab";
	say(s.repeatedStringMatch(sa, sb));
	return 0;
}



#include "aux.cpp"
#include "76.minimum-window-substring.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string ss = "ADOBECODEBANCCC", t="ABC";
	ss = "aaaaaaaaaaaabbbbbcdd", t = "abcdd";
	say(s.minWindow(ss, t));
	return 0;
}


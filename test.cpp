
#include "aux.cpp"
#include "467.unique-substrings-in-wraparound-string.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string ss = "zab"; 
	ss = "zaba";
	say(s.findSubstringInWraproundString(ss));
	return 0;
}


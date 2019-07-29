
#include "aux.cpp"
#include "680.valid-palindrome-ii.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string st = "deeeeeeee";
	// st = "abcdefedbcba";
	st = "abcbdda";

	say(s.validPalindrome(st));
	return 0;
}


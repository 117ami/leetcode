
#include "aux.cpp"
#include "5.longest-palindromic-substring.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string st = "abcba"; 
	string res = s.longestPalindrome(st);
	say(res);
	return 0;
}


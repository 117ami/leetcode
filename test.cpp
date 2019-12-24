
#include "aux.cpp"
#include "32.longest-valid-parentheses.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string t = "())()())";
	say(s.longestValidParentheses(t));
	return 0;
}


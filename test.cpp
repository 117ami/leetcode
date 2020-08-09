
#include "aux.cpp"
#include "1541.minimum-insertions-to-balance-a-parentheses-string.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string ss = "))())("; 
	ss = "(()))";
	say(s.minInsertions(ss));
	return 0;
}


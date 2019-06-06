
#include "aux.cpp"
#include "c.cpp"
#include "151.reverse-words-in-a-string.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	say(s.reverseWords(" the   is this  blue "));
	VS arr{"the", "is", "the"};
	return 0;
}


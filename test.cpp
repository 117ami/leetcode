
#include "aux.cpp"
#include "1249.minimum-remove-to-make-valid-parentheses.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string ss = "a(b(c(d)e)f";
	say(s.minRemoveToMakeValid(ss));
	return 0;
}


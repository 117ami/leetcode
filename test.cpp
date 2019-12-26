
#include "aux.cpp"
#include "14.longest-common-prefix.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vs ss {"flower", "flow", "flight"};
	// ss = {"a", "b"};
	ss = {"a", "a"};
	say(s.longestCommonPrefix(ss));
	string t ="12345"; 
	say(t.substr(0,3));
	return 0;
}


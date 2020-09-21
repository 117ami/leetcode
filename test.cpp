
#include "aux.cpp"
#include "1593.split-a-string-into-the-max-number-of-unique-substrings.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string text = "ababccc" ;
	// text="aa";
	// say(text.substr(2));
	say(s.maxUniqueSplit(text));
	return 0;
}


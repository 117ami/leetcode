
#include "aux.cpp"
#include "c.cpp"
#include "336.palindrome-pairs.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	VS words = {"abcd", "dcba", "lls", "s", "sssll", ""};
	words = {"a","abc","aba",""};
	// words = {"abcd", "dcba", "ss"};
	for(auto &pair: s.palindromePairs(words)) say(pair);
	return 0;
}



#include "aux.cpp"
#include "1170.compare-strings-by-frequency-of-the-smallest-character.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vs queries = {"bbb", "cc"}, words = {"a", "aaa", "aa", "aaaa"};
	s.numSmallerByFrequency(queries, words);
	return 0;
}


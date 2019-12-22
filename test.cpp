
#include "aux.cpp"
#include "5293.maximum-number-of-occurrences-of-a-substring.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string ss = "aababcaab"; 
	int maxLetters = 2, minSize = 3, maxSize = 4; 
	say(s.maxFreq(ss, maxLetters, minSize, maxSize));

	return 0;
}



#include "aux.cpp"
#include "c.cpp"
#include "5083.occurrences-after-bigram.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string text = "we will we will rock you", first = "we", second = "will"; 
	text = "alice is a good girl she is a good student", first = "a", second = "good";
	say(s.findOcurrences(text, first, second));
	return 0;
}


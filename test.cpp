
#include "aux.cpp"
#include "1160.find-words-that-can-be-formed-by-characters.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<string> words = {"cat","bt","hat","tree"}; 
	string chars = "atach";
	say(s.countCharacters(words, chars)); 
	return 0;
}


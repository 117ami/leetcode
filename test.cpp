
#include "aux.cpp"
#include "953.verifying-an-alien-dictionary.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vs words = {"word","world","row"} ;
	string order = "worldabcefghijkmnpqstuvxyz";
	say(s.isAlienSorted(words, order));
	return 0;
}


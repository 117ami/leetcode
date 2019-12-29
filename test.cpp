
#include "aux.cpp"
#include "127.word-ladder.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string b = "hit", e = "cog"; 
	vs wl = {"hot", "dot", "dog", "lot", "log", "cog"};
	say(s.ladderLength(b,e,wl));
	return 0;
}


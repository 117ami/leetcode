
#include "aux.cpp"
#include "691.stickers-to-spell-word.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vs stickers = {"with", "example", "science"}; 
	string target = "thehat";
	say(s.minStickers(stickers, target));
	return 0;
}




#include "aux.cpp"
#include "1344.jump-game-v.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi arr = {6,4,14,6,8,13,9,7,10,6,12}; 
	int d = 2; 
	say(s.maxJumps(arr, d));
	return 0;
}


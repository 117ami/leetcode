
#include "aux.cpp"
#include "1510.stone-game-iv.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	forloopup(i, 1, 18)
		say(s.winnerSquareGame(i));
	return 0;
}


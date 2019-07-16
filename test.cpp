
#include "aux.cpp"
#include "950.reveal-cards-in-increasing-order.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi d {17,13,11,2,3,5,7};
	say(s.deckRevealedIncreasing(d));
	return 0;
}


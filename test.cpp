
#include "aux.cpp"
#include "1402.reducing-dishes.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi sa = {3,4,2};
	sa = {-1,-8,0,5,-9};
	sa = {-2,5,-1,0,3,-3};
	say(s.maxSatisfaction(sa));
	return 0;
}


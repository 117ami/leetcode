
#include "aux.cpp"
#include "c.cpp"
#include "475.heaters.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi houses = {1,2,3}, heaters={2};
	say(s.findRadius(houses, heaters));
	return 0;
}


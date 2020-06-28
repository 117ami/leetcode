
#include "aux.cpp"
#include "332.reconstruct-itinerary.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvs xx = {{"JFK", "A"}};
	say(s.findItinerary(xx));
	return 0;
}


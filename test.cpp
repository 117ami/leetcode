
#include "aux.cpp"
#include "c.cpp"
#include "1094.car-pooling.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvi trips = {{3,2,7},{3,7,9},{8,3,9}}; 
	int capacity = 10; 
	say(s.carPooling(trips, capacity));
	return 0;
}


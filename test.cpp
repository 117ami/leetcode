
#include "aux.cpp"
#include "853.car-fleet.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	int target = 12 ;
	std::vector<int> position = {10,8,0,5,3} ;
	std::vector<int> speed = {2,4,1,1,3} ;
	position={8,12,16,11,7}; 
	speed = {6,9,10,9,7};
	say(s.carFleet(17,position, speed));


	return 0;
}


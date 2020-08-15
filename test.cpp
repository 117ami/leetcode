
#include "aux.cpp"
#include "1488.avoid-flood-in-the-city.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<int> r = {1,2,0,0,2,1}; 
	// r = {1,2,0, 2};
	// r = {42, 0,0,42};
	say(s.avoidFlood(r));
	return 0;
}


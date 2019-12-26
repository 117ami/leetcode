
#include "aux.cpp"
#include "1223.dice-roll-simulation.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	int n = 3; 
	vi roll={1,1,1,2,2,3};
	// n=2, roll={1,1,2,2,2,3};
	n=5000, roll={13, 3, 12, 14, 11, 11};
	say(s.dieSimulator(n, roll));
	return 0;
}


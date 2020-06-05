
#include "aux.cpp"
#include "528.random-pick-with-weight.cpp"

int main(int argc, char const *argv[]) {
	vector<int> x = {1, 3};
	Solution s(x);
	for (int i=0;i<10;i++)
		say(s.pickIndex());
	return 0;
}


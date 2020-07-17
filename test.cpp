
#include "aux.cpp"
#include "347.top-k-frequent-elements.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi t = {1,22,2,1,2,1,2,1,2,1,11}; 
	say(s.topKFrequent(t, 2));
	return 0;
}


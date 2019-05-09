
#include "aux.cpp"
#include "56.merge-intervals.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	std::vector<std::vector<int> > intervals = {{1,3},{2,6},{8,10}, {2, 4},{15,18}};
	s.merge(intervals);
	return 0;
}


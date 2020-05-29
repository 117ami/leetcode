
#include "aux.cpp"
#include "207.course-schedule.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<vector<int>> pre = {{1, 0}, {3, 0}, {1, 3}, {2, 1}};
	say(s.canFinish(4, pre));
	return 0;
}



#include "aux.cpp"
#include "210.course-schedule-ii.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvi p = {{3, 1}, {3, 2}, {1, 0}, {2, 0}}; 
	say(s.findOrder(4, p));
	return 0;
}


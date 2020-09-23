
#include "aux.cpp"
#include "1462.course-schedule-iv.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	// int n = 2 ;
	// std::vector<vector<int>> prerequisites = {{1,0}} ;
	// std::vector<vector<int>> queries = {{0,1},{1,0}} ;

	// int n = 2 ;
	// std::vector<int> prerequisites = {} ;
	// std::vector<vector<int>> queries = {{1,0},{0,1}} ;

	// int n = 3 ;
	// std::vector<vector<int>> prerequisites = {{1,2},{1,0},{2,0}} ;
	// std::vector<vector<int>> queries = {{1,0},{1,2}} ;

	// int n = 3 ;
	// std::vector<vector<int>> prerequisites = {{1,0},{2,0}} ;
	// std::vector<vector<int>> queries = {{0,1},{2,0}} ;

	int n = 5 ;
	std::vector<vector<int>> prerequisites = {{0,1},{1,2},{2,3},{3,4}} ;
	std::vector<vector<int>> queries = {{0,4},{4,0},{1,3},{3,0}} ;
	say(s.checkIfPrerequisite(n, prerequisites, queries));


	return 0;
}


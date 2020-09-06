
#include "aux.cpp"
#include "1575.count-all-possible-routes.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	// std::vector<int> locations = {2,3,6,8,4} ;
	// int start = 1 ;
	// int finish = 3 ;
	// int fuel = 5 ;

	// std::vector<int> locations = {4,3,1} ;
	// int start = 1 ;
	// int finish = 0 ;
	// int fuel = 6 ;

	// std::vector<int> locations = {5,2,1} ;
	// int start = 0 ;
	// int finish = 2 ;
	// int fuel = 3 ;

	// std::vector<int> locations = {2,1,5} ;
	// int start = 0 ;
	// int finish = 0 ;
	// int fuel = 3 ;

	std::vector<int> locations = {1,2,3} ;
	int start = 0 ;
	int finish = 2 ;
	int fuel = 40 ;

	say(s.countRoutes(locations, start, finish, fuel));
	return 0;
}


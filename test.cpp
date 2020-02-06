
#include "aux.cpp"
#include "1333.filter-restaurants-by-vegan-friendly-price-and-distance.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvi rest = extractMatrixFromString("[[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]"); 
	say(s.filterRestaurants(rest, 0, 50, 10));
	return 0;
}


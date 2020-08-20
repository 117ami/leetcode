
#include "aux.cpp"
#include "787.cheapest-flights-within-k-stops.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	std::vector<vector<int>> ns= {{0,1,100},{1,2,100}, {0,2,500}};
	// ns = {{4,1,1},{1,2,3},{0,3,2},{0,4,10},{3,1,1},{1,4,3}};
	// ns = {{1, 0, 5}};
	// ns = {{0,1,1}, {1,2,1}, {0, 2, 5}, {2, 3, 1}};
	say(s.findCheapestPrice(3, ns, 0, 2, 1));
	// say(s.findCheapestPrice(5, ns, 2, 1, 1));

	    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>,
                   greater<tuple<int, int, int>>>
        pq;

	return 0;
}


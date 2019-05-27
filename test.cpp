
#include "aux.cpp"
#include "c.cpp"

int main(int argc, char const *argv[]) {
	int a = 10, b = 9; 
	VI v = {1, 3, 2, 3, 8, 9};

	VVI vv = {{1, 2}, {5, 3}, {9, 10}, {4, 5}, {4, 3}, {2, 3}};
	sort_by_last(vv);
	say(vv);

	VI rv = randvector(100, 9);
	say(rv);
	LL rvsum = product(rv);
	say(rvsum);

	int nmax = vec_max(rv);
	int nmin = vec_min(rv);	
	say(VI {nmax, nmin});
}


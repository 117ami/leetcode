
#include "aux.cpp"
// #include "c.cpp"
#include "1286.iterator-for-combination.cpp"

using vvc = vector<vector<char>>; 

int main(int argc, char const *argv[]) {
	CombinationIterator ci("aaaaaaaabbaabb", 8);
	while(ci.hasNext()) say(ci.next());
	// vi a = {1, 2, 3, 4}; 
	// vc b = {'a', 'b', 'c'};
	// vvc ans; 
	// vc tmp; 
	// int n = 4, k = 2; 
	// makeCombiUtil(ans, b, tmp, 0, k);
	// say(ans);
	// vc a = {'c', 'a', 'a', 'b'};
	
	// do {
	// 	say(a);
	// } while (next_permutation(a.begin(), a.end()) );
	return 0;
}


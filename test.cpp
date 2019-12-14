
#include "aux.cpp"
#include "1175.prime-arrangements.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	int res = 0; 
	forup(i, 1, 101) {
		res = s.numPrimeArrangements(i);
		cout << i << ":" << res << ", "; 
	}
	res = s.numPrimeArrangements(5);
	say(res);
	return 0;
}


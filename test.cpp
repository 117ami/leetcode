
#include "aux.cpp"
#include "1505.minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string c = "43432"; 
	int n =3;
	c = "3112056788886886880368579471175675";
	c = "434332";
	n =40;

	say(s.minInteger(c, n));


	std::vector<int> foo = {8,8,8,8,6,8,9,8,9,8};
	std::vector<int> cc(foo.size());
	std::iota(cc.begin(), cc.end(), 0);
	std::vector<int> bar;

	// copy only positive numbers:
	bool valid = true; 
	std::copy_if (cc.begin(), cc.end(), std::back_inserter(bar), [&foo, &valid](int i){ 
		// valid = i > 0 && foo[i] > foo[i-1] ? false : valid; 
		return foo[i] == 8 && (valid &= (i == 0 || (i > 0 && foo[i] <= foo[i-1]) ));
		// (i == 0 || (i > 0 && valid ));
		} );
	say(bar);
	return 0;
}


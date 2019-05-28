
#include "aux.cpp"
#include "c.cpp"
#include "1054.distant-barcodes.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	VI b = {1,1,1,1,2,2,3,3};
	say(s.rearrangeBarcodes(b));
	return 0;
}


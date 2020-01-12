
#include "aux.cpp"
#include "1313.decompress-run-length-encoded-list.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi ns = {1,2,3,4};
	say(s.decompressRLElist(ns));
	return 0;
}


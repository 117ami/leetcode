
#include "aux.cpp"
#include "535.encode-and-decode-tinyurl.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	say(s.decode(s.encode("www.google.com/29398437lsddajf;dsaj")));
	return 0;
}


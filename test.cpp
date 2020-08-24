
#include "aux.cpp"
#include "1032.stream-of-characters.cpp"

int main(int argc, char const *argv[]) {
	vs cs = {"cd", "f", "kl"};
	cs = {"ab", "ba", "aaab", "abab", "baa"};
	StreamChecker sc(cs);
	string xx = "aaaaa";
	for(auto c: xx){
		cout << c << " " << sc.query(c) << endl; 
	}

	return 0;
}


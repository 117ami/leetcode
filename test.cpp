
#include "aux.cpp"
#include "49.group-anagrams.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vs x = {"eat", "tea", "tan", "ate", "nat", "bat"};
	vvs y = s.groupAnagrams(x); 
	say(y);
	return 0;
}


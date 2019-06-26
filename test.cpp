
#include "aux.cpp"
#include "c.cpp"
#include "744.find-smallest-letter-greater-than-target.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vc letters{'c', 'f', 'k'}; 
	char target = 'k';
	say(s.nextGreatestLetter(letters, target));
	return 0;
}


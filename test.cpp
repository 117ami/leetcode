
#include "aux.cpp"
#include "900.rle-iterator.cpp"

int main(int argc, char const *argv[]) {
	vi A = {3,8,0,9,2,5};
	RLEIterator rle(A); 
	vi t = {2,1,1,2};
	for(auto i: t) say(rle.next(i));
	return 0;
}


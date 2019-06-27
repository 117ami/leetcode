
#include "aux.cpp"
#include "c.cpp"
#include "378.kth-smallest-element-in-a-sorted-matrix.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvi matrix = {{1,5,9},{10,11,13},{12,13,15}}; 
	int k = 7; 
	say(s.kthSmallest(matrix, k));
	return 0;
}


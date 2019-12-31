
#include "aux.cpp"
#include "354.russian-doll-envelopes.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvi es = extractMatrixFromString("[[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]");
	// es = extractMatrixFromString("[[5, 4], [6, 4], [6, 7], [2, 3]]");
	es = extractMatrixFromString("[[1,1],[1,1],[1,1]]");
	vi v1 = {1,1,1,4,5,510000};
	say(bisect_left(v1, 1));
	say(s.maxEnvelopes(es));
	return 0;
}


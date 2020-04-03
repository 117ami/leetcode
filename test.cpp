
#include "aux.cpp"
#include "388.longest-absolute-file-path.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string t = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext";
	say(s.lengthLongestPath(t));
	return 0;
}


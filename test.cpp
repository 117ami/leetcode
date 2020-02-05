
#include "aux.cpp"
#include "1335.minimum-difficulty-of-a-job-schedule.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi jobs = {11, 111, 22, 222, 33, 333, 44, 444}; int d = 6; 
	say(s.minDifficulty(jobs, d));
	return 0;
}


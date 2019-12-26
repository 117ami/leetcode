
#include "aux.cpp"
#include "478.generate-random-point-in-a-circle.cpp"

int main(int argc, char const *argv[]) {
	Solution *s = new Solution(0.01, 5.9, 3.4);
	fori(i,3){
		vector<double> vd = s->randPoint();
		say(vd);
	}

	return 0;
}



#include "aux.cpp"
#include "1487.making-file-names-unique.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vs x = {"wano","wano","wano","wano"};
	x = {"gta","gta(1)","gta","avalon"};
	say(s.getFolderNames(x));
	return 0;
}



#include "aux.cpp"
#include "c.cpp"


int main(int argc, char const *argv[]) {
	vi a = {1,2,3,7,4,6,4,3,6};
	dsort(a);
	say(a);
	auto idx = lower_bound(dall(a), 5);
	say(idx - a.begin());
	a.eb(999);
	say(a);
  return 0;
}

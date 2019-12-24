
#include "aux.cpp"
#include "732.my-calendar-iii.cpp"

int main(int argc, char const *argv[]) {
	MyCalendarThree* c = new MyCalendarThree();
	say(c->book(3, 10));
	say(c->book(4, 11));
	
	return 0;
}


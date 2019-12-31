
#include "aux.cpp"
#include "911.online-election.cpp"

int main(int argc, char const *argv[]) {
	vi persons = {0, 1, 1, 0, 0, 1, 0}, times = {0, 5, 10, 15, 20, 25, 30}; 
	TopVotedCandidate *t = new TopVotedCandidate(persons, times); 
	say(t->q(1));
	return 0;
}


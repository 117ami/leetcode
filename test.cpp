
#include "aux.cpp"
#include "1592.rearrange-spaces-between-words.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string text = "  this   is  a sentence " ;

	// string text = " practice   makes   perfect" ;

	// string text = "hello   world" ;

	// string text = "  walks  udp package   into  bar a" ;

	// text = "   a" ;
	string res = s.reorderSpaces(text); 
	say(res.size());
	say(res);


	return 0;
}


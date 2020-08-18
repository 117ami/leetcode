
#include "aux.cpp"
#include "30.substring-with-concatenation-of-all-words.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string ss = "wordgoodgoodgoodbestword"; 
	vector<string> vs  = {"word", "good", "best", "good"};
	// vs = {"hat", "red","bad", "cat", "red"};
	say(s.findSubstring(ss, vs));
	say(std::hash<std::string_view>{}(string_view(&ss[0], 4)));
	size_t ghash = 0;
	for (int i = 0; i < vs.size(); i++) {
		ghash += std::hash<std::string>{}(vs[i]); // construct a hash object and call the operator();
		say(ghash);
	}
	return 0;
}


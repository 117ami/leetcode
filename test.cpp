
#include "aux.cpp"
#include "1125.smallest-sufficient-team.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	std::vector<string> skills = {"algorithms","math","java","reactjs","csharp","aws"};
	std::vector<vector<string>> people = {{"algorithms","math","java"}, 
	{"algorithms","math","reactjs"}, {"java","csharp","aws"}, {"reactjs","csharp"}
	,{"csharp","math"}, {"aws","java"}};
	say(s.smallestSufficientTeam(skills, people));
	return 0;
}


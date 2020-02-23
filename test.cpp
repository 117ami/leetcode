
#include "aux.cpp"
#include "1360.number-of-days-between-two-dates.cpp"

// vector<string> split(string s, string delimiter){
// 	size_t pos = 0;
// 	vector<string> res ; 
// 	std::string token;
// 	while ((pos = s.find(delimiter)) != std::string::npos) {
// 		token = s.substr(0, pos);
// 		res.push_back(token);
// 		std::cout << token << std::endl;
// 		s.erase(0, pos + delimiter.length());
// 	}
// 	res.push_back(s);
// 	return res; 
// }

int main(int argc, char const *argv[]) {
	Solution s;
	string ss = "2020-09-12";
	string t = "2020-09-23";
	ss = "1971-06-29", t = "2010-09-23";
	ss = "2074-09-12", t = "1983-01-08";
	say(s.daysBetweenDates(ss, t));
	return 0;
}


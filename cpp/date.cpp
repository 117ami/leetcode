

class CppDate {
public:
  bool is_leap_year(int year) {
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
  }

  int day_of_year(string date) {
    int days[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int year = stoi(date.substr(0, 4)), m = stoi(date.substr(5, 2)),
        d = stoi(date.substr(8, 2));
    days[1] += is_leap_year(year) ? 1 : 0;
    return d + std::accumulate(days, days + m - 1, 0);
  }

  int days_since_1900(string date) {
    int year = stoi(date.substr(0, 4));
    int cnt = day_of_year(date);
    // say(cnt);
    for (int past = 1900; past < year; past++)
      cnt += is_leap_year(past) ? 366 : 365;

    return cnt;
  }

  int daysBetweenDates(string date1, string date2) {
    return abs(days_since_1900(date1) - days_since_1900(date2));
  }
};

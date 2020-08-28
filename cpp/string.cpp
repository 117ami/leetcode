

bool is_subsequence(string s, string t) {
  // Whether s is subsequence (not substring) of t.
  // i.e., s = "abcd", t = "abced", then true;
  int pos = 0;
  for (auto c : s) {
    pos = t.find(c, pos);
    if (pos == string::npos)
      return false;
    pos++;
  }
  return true;
}
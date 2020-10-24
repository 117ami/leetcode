// Containers
#include <deque>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#include "conf.d/say.h"

using namespace std;
int dirs[5] = {-1, 0, 1, 0, -1};

// --------------------------------------------------------
/**
 * // This is the HtmlParser's API interface.
 * // You should not implement it, or speculate about its implementation
 * class HtmlParser {
 *   public:
 *     vector<string> getUrls(string url);
 * };
 */

class Solution {
public:
  vector<string> crawl(string startUrl, HtmlParser htmlParser) {
    std::unordered_set<string> visited;
    visited.insert(startUrl);
    std::queue<string> todos;
    todos.push(startUrl);
    string host = startUrl.substr(0, startUrl.find("/", 7));

    while (!todos.empty()) {
      auto cur = todos.front();
      todos.pop();
      for (const auto &nxt : htmlParser.getUrls(cur)) {
        if (nxt.find(host) == 0 && visited.count(nxt) == 0) {
          visited.insert(nxt);
          todos.push(nxt);
        }
      }
    }

    return std::vector<string>(visited.begin(), visited.end());
  }
};

int main() { Solution s; }
// Containers
#include <deque>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <iostream>
#include <numeric>


#include "conf.d/say.h"

using namespace std; 
int dirs[5] = {-1, 0, 1, 0, -1};

// --------------------------------------------------------
class BoundedBlockingQueue {
public:
    int capacity; 
    std::mutex m; 
    std::condition_variable cv;
    std::queue<int> q; 

    BoundedBlockingQueue(int _capacity): capacity(_capacity) {}
    
    void enqueue(int element) {
      std::unique_lock<std::mutex> ul(m);
      while (this->size() >= capacity) cv.wait(ul);
      q.push(element);
      cv.notify_all();
    }
    
    int dequeue() {
      std::unique_lock<std::mutex> ul(m);
      while (this->size() == 0) cv.wait(ul);
      int e = q.front();
      q.pop();
      cv.notify_all();
      return e;
    }
    
    int size() {
        return q.size();
    }
};


int main() {
  Solution s;
  
}
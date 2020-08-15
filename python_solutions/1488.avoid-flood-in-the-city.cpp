/*
 * @lc app=leetcode id=1488 lang=cpp
 *
 * [1488] Avoid Flood in The City
 *
 * https://leetcode.com/problems/avoid-flood-in-the-city/description/
 *
 * algorithms
 * Medium (25.27%)
 * Total Accepted:    9.6K
 * Total Submissions: 38.1K
 * Testcase Example:  '[1,2,3,4]'
 *
 * Your country has an infinite number of lakes. Initially, all the lakes are
 * empty, but when it rains over the nth lake, the nth lake becomes full of
 * water. If it rains over a lake which is full of water, there will be a
 * flood. Your goal is to avoid the flood in any lake.
 *
 * Given an integer array rains where:
 *
 *
 * rains[i] > 0 means there will be rains over the rains[i] lake.
 * rains[i] == 0 means there are no rains this day and you can choose one lake
 * this day and dry it.
 *
 *
 * Return an array ans where:
 *
 *
 * ans.length == rains.length
 * ans[i] == -1 if rains[i] > 0.
 * ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
 *
 *
 * If there are multiple valid answers return any of them. If it is impossible
 * to avoid flood return an empty array.
 *
 * Notice that if you chose to dry a full lake, it becomes empty, but if you
 * chose to dry an empty lake, nothing changes. (see example 4)
 *
 *
 * Example 1:
 *
 *
 * Input: rains = [1,2,3,4]
 * Output: [-1,-1,-1,-1]
 * Explanation: After the first day full lakes are [1]
 * After the second day full lakes are [1,2]
 * After the third day full lakes are [1,2,3]
 * After the fourth day full lakes are [1,2,3,4]
 * There's no day to dry any lake and there is no flood in any lake.
 *
 *
 * Example 2:
 *
 *
 * Input: rains = [1,2,0,0,2,1]
 * Output: [-1,-1,2,1,-1,-1]
 * Explanation: After the first day full lakes are [1]
 * After the second day full lakes are [1,2]
 * After the third day, we dry lake 2. Full lakes are [1]
 * After the fourth day, we dry lake 1. There is no full lakes.
 * After the fifth day, full lakes are [2].
 * After the sixth day, full lakes are [1,2].
 * It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another
 * acceptable scenario.
 *
 *
 * Example 3:
 *
 *
 * Input: rains = [1,2,0,1,2]
 * Output: []
 * Explanation: After the second day, full lakes are  [1,2]. We have to dry one
 * lake in the third day.
 * After that, it will rain over lakes [1,2]. It's easy to prove that no matter
 * which lake you choose to dry in the 3rd day, the other one will flood.
 *
 *
 * Example 4:
 *
 *
 * Input: rains = [69,0,0,0,69]
 * Output: [-1,69,1,1,-1]
 * Explanation: Any solution on one of the forms [-1,69,x,y,-1], [-1,x,69,y,-1]
 * or [-1,x,y,69,-1] is acceptable where 1 <= x,y <= 10^9
 *
 *
 * Example 5:
 *
 *
 * Input: rains = [10,20,20]
 * Output: []
 * Explanation: It will rain over lake 20 two consecutive days. There is no
 * chance to dry any lake.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= rains.length <= 10^5
 * 0 <= rains[i] <= 10^9
 *
 */

#include <vector>

// class Solution {
// public:
//     vector<int> avoidFlood(vector<int>& rains) {
//         set<int> dry;
//         vector<int> res;
//         unordered_map<int, int> full;
//         for (int i = 0; i< rains.size(); i++){
//             if (0 == rains[i]) {
//                 res.emplace_back(1);
//                 dry.insert(i);
//             } else {
//                 int lake = rains[i];
//                 if (full.find(lake) != full.end()) {
//                     int j = full[lake];
//                     auto it = dry.lower_bound(j);
//                     if (it == dry.end()) return {};
//                     int k = *it;
//                     res[k] = lake;
//                     dry.erase(it);
//                 }
//                 full[lake] = i;
//                 res.emplace_back(-1);
//             }
//         }
//         return res;
//     }
// };

struct DisjointSet {
    vector<int> data;
    
    DisjointSet(int size) {
        data.reserve(size);
        for (int i = 0; i < size; i++) {
            data.push_back(i);
        }
    }
    
    /* For this problem, data[i] points to the index of next available dry day,
     or the index of index of next dry day, or ... A day is a dry day iff 
     data[i] == i. When a dry day i is used, the index should be updated to i+1 to
     point to the next potential dry day, this is what the merge operation does.
    */
    int find(int i) {
        return data[i] == i? i: data[i] = find(data[i]);
    }
    
    void merge(int i) {
        data[i] = i + 1;
    }
};

class Solution {
public:
    vector<int> avoidFlood(vector<int>& rains) {
        int days = rains.size();

        unordered_map<int, int> fills; // lake -> day
        DisjointSet ds(days);
        
        for (int i = 0; i < days; i++) {
            int lake = rains[i];
            if (lake > 0) {
                auto it = fills.find(lake);
                if (it != fills.end()) {
                    int dry_day = ds.find(fills[lake]);
                    // say(ds.data);
                    // say(vector{dry_day, i});
                    if (dry_day < i) {
                        rains[dry_day] = lake;
                        ds.merge(dry_day);
                    } else {
                        return {};
                    }
                }
                fills[lake] = i;
                rains[i] = -1;
                ds.merge(i);
                say(i);
                say(ds.data);
            } else {
                rains[i] = 1;
            }
        }
        return std::move(rains);
    }
};


auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();

// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem
// Medium (Difficulty)

// Given a list of folders, remove all sub-folders in those folders and return
// in any order the folders after removing. If a folder[i] is located
// within another folder[j], it is called a sub-folder of it. The format of a
// path is one or more concatenated strings of the form: / followed by one or
// more lowercase English letters. For
// example, /leetcode and /leetcode/problems are valid paths while an empty
// string and / are not.   Example 1: Example 2: Example 3:   Constraints:
// Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
// Output: ["/a","/c/d","/c/f"]
// Explanation: Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of
// folder "/c/d" in our filesystem.
//
// Input: folder = ["/a","/a/b/c","/a/b/d"]
// Output: ["/a"]
// Explanation: Folders "/a/b/c" and "/a/b/d/" will be removed because they are
// subfolders of "/a".
//
// Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
// Output: ["/a/b/c","/a/b/ca","/a/b/d"]
//
// xxxxxxxxxx
// class Solution {
// public:
//     vector<string> removeSubfolders(vector<string>& folder) {
//         
//     }
// };

class Solution {
public:
  vector<string> removeSubfolders(vector<string> &folder) {
    vector<string> ans;
    sort(folder.begin(), folder.end());
    ans.push_back(folder[0]);

    for (size_t i = 1; i < folder.size(); ++i) {
      string r = ans[ans.size() - 1] + "/";
      if (folder[i].substr(0, r.size()) != r)
        ans.push_back(folder[i]);
    }
    return ans;
  }
};

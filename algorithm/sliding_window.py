
def at_most(m, nums):
    '''Find the number of subarrays from nums such that the sum is no more than m
    '''
    if m < 0: return 0
    cnt, i, n = 0, 0, len(nums)
    for j in range(n):
        m -= nums[j]
        while m < 0:
            m += nums[i]
            i += 1
        cnt += j - i + 1
    return cnt

# Corresponding C++ 
# int atmost(int m, vector<int> &ns) {
#     if (m<0) return 0; 
#     int n = ns.size(), i = 0, cnt = 0; 
#     for(int j = 0; j < n; j ++) {
#         m -= ns[j]; 
#         while (m < 0) m += ns[i++];
#         cnt += j - i + 1; 
#     }
#     return cnt; 
# }


# Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher&#39;s h-index.
# According to the definition of h-index on Wikipedia: &quot;A scientist has index h if h of his/her N papers have at least h citations each, and the other N &minus; h papers have no more than h citations each.&quot;
# Example:
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
#              received 3, 0, 6, 1, 5 citations respectively.
# &nbsp;            Since the researcher has 3 papers with at least 3 citations each and the remaining
# &nbsp;            two with no more than 3 citations each, her h-index is 3.
# Note:&nbsp;If there are several possible values for h, the maximum one is taken as the h-index.
#

# @param {Integer[]} citations
# @return {Integer}
def h_index(citations)
  citations = citations.sort.reverse
  i = r = 0
  while i <= citations.size - 1
    r = [r, [i + 1, citations[i]].min].max
    break if i + 1 > citations[i]
    i += 1
  end
  r
end

citations = [3, 0, 6, 1, 5]
citations = [3, 2, 6, 4, 5]
citations = 10.times.map { Random.rand(10) }
# citations = [1]
p citations.sort.reverse
p h_index(citations)

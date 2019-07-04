# Given an array of citations sorted&nbsp;in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher&#39;s h-index.
# According to the&nbsp;definition of h-index on Wikipedia: &quot;A scientist has index&nbsp;h&nbsp;if&nbsp;h&nbsp;of his/her&nbsp;N&nbsp;papers have&nbsp;at least&nbsp;h&nbsp;citations each, and the other&nbsp;N &minus; h&nbsp;papers have&nbsp;no more than&nbsp;h&nbsp;citations each.&quot;
# Example:
# Input: citations = [0,1,3,5,6]
# Output: 3
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had
#              received 0, 1, 3, 5, 6 citations respectively.
# &nbsp;            Since the researcher has 3 papers with at least 3 citations each and the remaining
# &nbsp;            two with no more than 3 citations each, her h-index is 3.
# Note:
# If there are several possible values for&nbsp;h, the maximum one is taken as the h-index.
# Follow up:
#   This is a follow up problem to&nbsp;H-Index, where citations is now guaranteed to be sorted in ascending order.
#   Could you solve it in logarithmic time complexity?
#

# @param {Integer[]} citations
# @return {Integer}
def h_index(citations)
  # return 0 if citations.empty?
  xsize = citations.size
  xsize - ((0..xsize - 1).bsearch { |i| citations[i] >= xsize - i } || xsize)
end

citations = [0, 1, 3, 5, 6]
citations = 10.times.map { Random.rand(10) }.sort
citations = [0, 0, 0]
citations = []
p citations
p h_index(citations)

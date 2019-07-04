

# @param {String[]} strs
# @return {Integer}
def find_lu_slength(strs)
  strs.sort_by!(&:length).reverse!
  (0..strs.size - 1).each do |i|
    uncommon = true
    (0..strs.size - 1).each do |j|
      next if i == j
      break if strs[i].length > strs[j].length
      if subsequence?(strs[i], strs[j])
        uncommon = false
        break
      end
    end
    return strs[i].length if uncommon
  end
  -1
end

def subsequence?(stseq, lgseq)
  return true if stseq == ''
  return false if stseq.length > lgseq.length
  i = 0
  i += 1 while i < lgseq.length && lgseq[i] != stseq[0]
  return false if i == lgseq.length
  subsequence?(stseq[1..stseq.length - 1], lgseq[i + 1..lgseq.length - 1])
end

strs = %w[aaa aaa aa]
strs = %w[aabbccd aabbcc cb]
p find_lu_slength(strs)

sa = 'abaabbcc'
sb = 'bbabcc'
p subsequence?(sb, sa)

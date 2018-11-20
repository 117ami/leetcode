# Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
# Now, we would like to merge these accounts.  Two accounts definitely belong to the same person if there is some email that is common to both accounts.  Note that even if two accounts have the same name, they may belong to different people as people could have the same name.  A person can have any number of accounts initially, but all of their accounts definitely have the same name.
# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order.  The accounts themselves can be returned in any order.
# Example 1:
# Input:
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# Explanation:
# The first and third John's are the same person as they have the common email "johnsmith@mail.com".
# The second John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
# Note:
# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].

# @param {String[][]} accounts
# @return {String[][]}
def accounts_merge(accounts)
  parent = Array(0..1001)
  find = lambda do |i|
    return i if i == parent[i]
    find.call(parent[i])
  end

  owner = {}
  (0..accounts.size * 4 - 1).each do |i|
    i = i % accounts.size
    acc = accounts[i]
    acc[1..-1].each do |m|
      parent[owner[m]] = parent[i] = [find.call(i), find.call(owner[m])].min if owner.key?(m)
      owner[m] = parent[i]
    end
  end

  merged = []
  owner.each_pair do |k, v|
    pid = find.call(v)
    merged[pid] = [accounts[pid].first] if merged[pid].nil?
    merged[pid] << k
  end
  merged.compact.map(&:sort)
end

accounts = [['John', 'johnsmith@mail.com', 'john00@mail.com'], ['John', 'johnnybravo@mail.com'], ['John', 'johnpp@i.com'], ['John', 'john_newyork@mail.com', 'johnsmith@mail.com', 'johnpp@i.com'], ['Mary', 'mary@mail.com']]

# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

# accounts = [['David', 'David0@m.co', 'David1@m.co'], ['David', 'David3@m.co', 'David4@m.co'], ['David', 'David4@m.co', 'David5@m.co'], ['David', 'David2@m.co', 'David3@m.co'], ['David', 'David1@m.co', 'David2@m.co']]

# accounts = [["Bob","Bob90@m.co","Bob91@m.co"],["Bob","Bob66@m.co","Bob67@m.co"],["Bob","Bob59@m.co","Bob60@m.co"],["Bob","Bob17@m.co","Bob18@m.co"],["Bob","Bob9@m.co","Bob10@m.co"],["Bob","Bob94@m.co","Bob95@m.co"],["Bob","Bob42@m.co","Bob43@m.co"],["Bob","Bob87@m.co","Bob88@m.co"],["Bob","Bob1@m.co","Bob2@m.co"],["Bob","Bob50@m.co","Bob51@m.co"],["Bob","Bob49@m.co","Bob50@m.co"],["Bob","Bob52@m.co","Bob53@m.co"],["Bob","Bob24@m.co","Bob25@m.co"],["Bob","Bob53@m.co","Bob54@m.co"],["Bob","Bob60@m.co","Bob61@m.co"],["Bob","Bob12@m.co","Bob13@m.co"],["Bob","Bob16@m.co","Bob17@m.co"],["Bob","Bob38@m.co","Bob39@m.co"],["Bob","Bob27@m.co","Bob28@m.co"],["Bob","Bob85@m.co","Bob86@m.co"],["Bob","Bob7@m.co","Bob8@m.co"],["Bob","Bob54@m.co","Bob55@m.co"],["Bob","Bob35@m.co","Bob36@m.co"],["Bob","Bob47@m.co","Bob48@m.co"],["Bob","Bob37@m.co","Bob38@m.co"],["Bob","Bob92@m.co","Bob93@m.co"],["Bob","Bob74@m.co","Bob75@m.co"],["Bob","Bob97@m.co","Bob98@m.co"],["Bob","Bob48@m.co","Bob49@m.co"],["Bob","Bob23@m.co","Bob24@m.co"],["Bob","Bob69@m.co","Bob70@m.co"],["Bob","Bob41@m.co","Bob42@m.co"],["Bob","Bob61@m.co","Bob62@m.co"],["Bob","Bob72@m.co","Bob73@m.co"],["Bob","Bob45@m.co","Bob46@m.co"],["Bob","Bob89@m.co","Bob90@m.co"],["Bob","Bob19@m.co","Bob20@m.co"],["Bob","Bob79@m.co","Bob80@m.co"],["Bob","Bob88@m.co","Bob89@m.co"],["Bob","Bob10@m.co","Bob11@m.co"],["Bob","Bob0@m.co","Bob1@m.co"],["Bob","Bob62@m.co","Bob63@m.co"],["Bob","Bob18@m.co","Bob19@m.co"],["Bob","Bob3@m.co","Bob4@m.co"],["Bob","Bob83@m.co","Bob84@m.co"],["Bob","Bob77@m.co","Bob78@m.co"],["Bob","Bob75@m.co","Bob76@m.co"],["Bob","Bob71@m.co","Bob72@m.co"],["Bob","Bob64@m.co","Bob65@m.co"],["Bob","Bob86@m.co","Bob87@m.co"],["Bob","Bob84@m.co","Bob85@m.co"],["Bob","Bob33@m.co","Bob34@m.co"],["Bob","Bob15@m.co","Bob16@m.co"],["Bob","Bob29@m.co","Bob30@m.co"],["Bob","Bob22@m.co","Bob23@m.co"],["Bob","Bob63@m.co","Bob64@m.co"],["Bob","Bob81@m.co","Bob82@m.co"],["Bob","Bob68@m.co","Bob69@m.co"],["Bob","Bob25@m.co","Bob26@m.co"],["Bob","Bob78@m.co","Bob79@m.co"],["Bob","Bob80@m.co","Bob81@m.co"],["Bob","Bob76@m.co","Bob77@m.co"],["Bob","Bob39@m.co","Bob40@m.co"],["Bob","Bob34@m.co","Bob35@m.co"],["Bob","Bob73@m.co","Bob74@m.co"],["Bob","Bob56@m.co","Bob57@m.co"],["Bob","Bob43@m.co","Bob44@m.co"],["Bob","Bob32@m.co","Bob33@m.co"],["Bob","Bob40@m.co","Bob41@m.co"],["Bob","Bob13@m.co","Bob14@m.co"],["Bob","Bob99@m.co","Bob100@m.co"],["Bob","Bob6@m.co","Bob7@m.co"],["Bob","Bob67@m.co","Bob68@m.co"],["Bob","Bob51@m.co","Bob52@m.co"],["Bob","Bob28@m.co","Bob29@m.co"],["Bob","Bob36@m.co","Bob37@m.co"],["Bob","Bob21@m.co","Bob22@m.co"],["Bob","Bob58@m.co","Bob59@m.co"],["Bob","Bob95@m.co","Bob96@m.co"],["Bob","Bob2@m.co","Bob3@m.co"],["Bob","Bob57@m.co","Bob58@m.co"],["Bob","Bob11@m.co","Bob12@m.co"],["Bob","Bob31@m.co","Bob32@m.co"],["Bob","Bob98@m.co","Bob99@m.co"],["Bob","Bob5@m.co","Bob6@m.co"],["Bob","Bob93@m.co","Bob94@m.co"],["Bob","Bob96@m.co","Bob97@m.co"],["Bob","Bob82@m.co","Bob83@m.co"],["Bob","Bob44@m.co","Bob45@m.co"],["Bob","Bob65@m.co","Bob66@m.co"],["Bob","Bob30@m.co","Bob31@m.co"],["Bob","Bob8@m.co","Bob9@m.co"],["Bob","Bob26@m.co","Bob27@m.co"],["Bob","Bob70@m.co","Bob71@m.co"],["Bob","Bob20@m.co","Bob21@m.co"],["Bob","Bob4@m.co","Bob5@m.co"],["Bob","Bob55@m.co","Bob56@m.co"],["Bob","Bob91@m.co","Bob92@m.co"],["Bob","Bob14@m.co","Bob15@m.co"],["Bob","Bob46@m.co","Bob47@m.co"]]

p accounts_merge(accounts)
p accounts_merge(accounts).size

# You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.
# For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.
# Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.
# Example 1:
# Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
# Output: 11
# Explanation:
# Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
# Note:
# One employee has at most one direct leader and may have several subordinates.
# The maximum number of employees won't exceed 2000.
#
#  https://leetcode.com/problems/employee-importance/description/

# Employee info
class Employee
  attr_accessor :id, :importance, :subordinates
  def initialize(id, importance, subordinates)
    # It's the unique id of each node.
    # unique id of this employee
    @id = id
    # the importance value of this employee
    @importance = importance
    # the id of direct subordinates
    @subordinates = subordinates
  end
end

# @param {Employee} employees
# @param {Integer} id
# @return {Integer}
def get_importance(employees, id)
  arr = employees.map { |e| [e.id, e.importance, e.subordinates] }
  impo = {}
  subo = {}
  arr.each do |a|
    idx, v, slaves = a
    impo[idx] = v
    subo[idx] = slaves
  end
  res = 0
  xarr = [id]
  until xarr.empty?
    idx = xarr.shift
    res += impo[idx]
    xarr += subo[idx]
  end
  res
end

ea = Employee.new(1, 5, [2, 3])
eb = Employee.new(2, 3, [])
ec = Employee.new(3, 3, [])
p get_importance([ea, eb, ec], 1)

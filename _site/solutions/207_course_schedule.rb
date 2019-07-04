# There are a total of n courses you have to take, labeled from 0 to n-1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
# Example 1:
# Input: 2, [[1,0]]
# Output: true
# Explanation:There are a total of 2 courses to take.
#             To take course 1 you should have finished course 0. So it is possible.
# Example 2:
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation:There are a total of 2 courses to take.
#             To take course 1 you should have finished course 0, and to take course 0 you should
#             also have finished course 1. So it is impossible.
# Note:
#   The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
#   You may assume that there are no duplicate edges in the input prerequisites.
#
#  https://leetcode.com/problems/course-schedule/description/
require './aux.rb'

# @param {Integer} num_courses
# @param {Integer[][]} prerequisites
# @return {Boolean}
def can_finish(num_courses, prerequisites)
  visit = [0] * num_courses
  graph = Array.new(num_courses) { [] }
  prerequisites.each { |a, b| graph[a] << b }
  dfs = lambda do |n|
    return false if visit[n] == -1
    return true if visit[n] == 1
    visit[n] = -1
    graph[n].each do |k|
      return false unless dfs.call(k)
    end
    visit[n] = 1
    return true
  end

  0.upto(num_courses - 1).each do |n|
    return false unless dfs.call(n)
  end
  true
end

num_courses = 8
prerequisites = [[0, 1], [1, 2], [2, 4], [1, 3], [3, 4], [3, 5], [5, 4], [7, 3], [5, 7]]
p can_finish(num_courses, prerequisites)

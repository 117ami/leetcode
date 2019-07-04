# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# For example,
# Given board =
#
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

# @param {Character[][]} board
# @param {String} word
# @return {Boolean}
require 'matrix'

def exist(board, word)
  return false if board.empty?
  Matrix.rows(board).each_with_index do |e, i, j|
    return true if dfs(board, i, j, word)
  end
  false
end

def dfs(board, i, j, word)
  return true if word.empty?
  return false if i < 0 || i > board.size - 1 ||
                  j < 0 || j > board[0].size - 1 ||
                  board[i][j] != word[0]
  tmp = board[i][j]
  board[i][j] = '*'
  r = dfs(board, i + 1, j, word[1..-1]) || dfs(board, i - 1, j, word[1..-1]) ||
      dfs(board, i, j + 1, word[1..-1]) || dfs(board, i, j - 1, word[1..-1])
  board[i][j] = tmp
  r
end

board = [
  %w[A B C E],
  %w[S F C S],
  %w[A D E E]
]

# board = [["C","A","A"],["A","A","A"],["B","C","D"]]
p exist(board, 'ABC')

Matrix.rows(board).each_with_index do |e, i, j|
  puts "#{[e, i, j]}"
  0.upto(board.size - 1) do |i|
    0.upto(board[0].size - 1) do |j|
      
    end
  end
end


# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
# A partially filled sudoku which is valid.
#
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

def valid_line?(row)
  h = Hash.new(0).tap { |hash| row.each { |v| hash[v] += 1 } }
  h.each do |k, v|
    next if k == '.'
    return false if v > 1 || k == 0
  end
  true
end

# @param {Character[][]} board
# @return {Boolean}
def is_valid_sudoku(board)
  0.upto(8).each do |i|
    return false unless valid_line?(board[i])
    col = Array(0..8).map { |j| board[j][i] }
    p board[i], col
    return false unless valid_line?(col)
  end

  a = [0, 1, 2]
  b = [3, 4, 5]
  c = [6, 7, 8]
  Array[a, b, c].each do |i|
    Array[a, b, c].each do |j|
      cor = i.product(j)
      row = cor.map { |v| board[v[0]][v[1]] }
      return false unless valid_line?(row)
    end
  end
  true
end

board = [['.', '8', '7', '6', '5', '4', '3', '2', '1'], ['2', '.', '.', '.', '.', '.', '.', '.', '.'], ['3', '.', '.', '.', '.', '.', '.', '.', '.'], ['4', '.', '.', '.', '.', '.', '.', '.', '.'], ['5', '.', '.', '.', '.', '.', '.', '.', '.'], ['6', '.', '.', '.', '.', '.', '.', '.', '.'], ['7', '.', '.', '.', '.', '.', '.', '.', '.'], ['8', '.', '.', '.', '.', '.', '.', '.', '.'], ['9', '.', '.', '.', '.', '.', '.', '.', '.']]

board = [["7",".",".",".","4",".",".",".","."],[".",".",".","8","6","5",".",".","."],[".","1",".","2",".",".",".",".","."],[".",".",".",".",".","9",".",".","."],[".",".",".",".","5",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".","2",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]

p is_valid_sudoku(board)


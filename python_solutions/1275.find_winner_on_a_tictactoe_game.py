
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/description/
# Easy


class Solution:
    def tictactoe(self, moves):
        if len(moves) < 5:
            return 'Pending'

        grids = [[''] * 3 for _ in range(3)]
        for i, m in enumerate(moves):
            grids[m[0]][m[1]] = 'O' if i & 1 else 'X'

        last_sys = 'X' if len(moves) & 1 else 'O'
        winner = 'A' if last_sys == 'X' else 'B'

        for i in range(3):
            if ''.join(grids[i]) == last_sys * \
                    3 or ''.join([grids[0][i], grids[1][i], grids[2][i]]) == last_sys * 3:
                return winner

        
        if ''.join([grids[0][0], grids[1][1], grids[2][2]]) == last_sys * \
                3 or ''.join([grids[2][0], grids[1][1], grids[0][2]]) == last_sys * 3:
            return winner
        
        return 'Draw' if len(moves) == 9 else 'Pending'



s = Solution()
moves = [[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]
moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
moves = [[1,0],[2,2],[2,0],[0,1],[1,1]]
moves = [[2,0],[1,1],[0,2],[2,1],[1,2],[1,0],[0,0],[0,1]]
print(s.tictactoe(moves))

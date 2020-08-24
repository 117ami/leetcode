from heapq import heappush, heappop
import itertools


class PriorityQueue:
    def __init__(self, iterable=[]):
        self.heap = []
        for value in iterable:
            heappush(self.heap, (0, value))

    def add(self, value, priority=0):
        heappush(self.heap, (priority, value))

    def pop(self):
        priority, value = heappop(self.heap)
        return value

    def __len__(self):
        return len(self.heap)


class AStar:
    def __init__(self, grid):
        self.grid = grid
        self.M = len(grid)
        self.N = len(grid[0])

    def a_star_graph_search(self, start=(0, 0)):
        ''' 
        '''
        if self.grid[0][0] == 1 or self.grid[self.M - 1][self.N - 1] == 1:
            return None

        visited = set()
        came_from = dict()
        distance = {start: 0}
        frontier = PriorityQueue()
        frontier.add(start)

        while frontier:
            node = frontier.pop()
            if node in visited:
                continue

            # Reach the target. Note: sometimes the target may be different
            # from the bottom-right node.
            if node == (self.M - 1, self.N - 1):
                return self._reconstruct_path(came_from, start, node)

            visited.add(node)
            for successor in self._get_8_directions_successors(node):
                frontier.add(successor,
                             priority=distance[node] + 1 +
                             self._get_heuristic(successor))
                if (successor not in distance
                        or distance[node] + 1 < distance[successor]):
                    distance[successor] = distance[node] + 1
                    came_from[successor] = node
        return None

    def _reconstruct_path(self, came_from, start, end):
        """ Construct the path from start to end 
        >>> came_from = {'b': 'a', 'c': 'a', 'd': 'c', 'e': 'd', 'f': 'd'}
        >>> _reconstruct_path(came_from, 'a', 'e')
        ['a', 'c', 'd', 'e']
        """
        reverse_path = [end]
        while end != start:
            end = came_from[end]
            reverse_path.append(end)
        return reverse_path[::-1]

    def _get_successors(self, node):
        """ Return a list of valid successors from node. 
        Depends on specific tasks, sometimes diagonal move is allowed
        """
        dirs = [-1, 0, 1, 0, -1]
        i, j = node
        for d in range(4):
            ni, nj = i + dirs[d], j + dirs[d + 1]
            if 0 <= ni < self.M and 0 <= nj < self.N and self.grid[ni][nj] == 0:
                yield (ni, nj)

    def _get_8_directions_successors(self, node):
        """ Return a list of valid successors from node.
        Depends on specific tasks, sometimes diagonal move is allowed
        """
        i, j = node
        for da, db in itertools.product((-1, 0, 1), (-1, 0, 1)):
            if not (da == 0 and db == 0):
                ni, nj = i + da, j + db
                if 0 <= ni < self.M and 0 <= nj < self.N and self.grid[ni][
                        nj] == 0:
                    yield (ni, nj)

    def _get_heuristic(self, node):
        """ Get heuristic cost of current node to the target. 
        The cost can be either Manhantan distance or L2 distance 
        """
        i, j = node
        return max(self.M - i, self.N - j)


if __name__ == "__main__":
    exa = [[0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 0, 1, 1, 0, 1, 0], [0, 1, 1, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 1, 1], [1, 0, 1, 0, 0, 0, 0, 0],
           [1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0]]
    sol = AStar(exa)
    res = sol.a_star_graph_search((0, 0))
    print(res)

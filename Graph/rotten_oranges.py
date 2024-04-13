from typing import List


class Solution:

    def bfs(visited, queue):
        node = queue.pop(0)
        # get near nodes
        row_d = [-1,0,1,0]
        col_d = [0,-1,0,1]
        for row,col in zip(row_d,col_d):
          if node[0]+row >0 and node[1]+col > 0 and node[1]+col < len(visited) and node[0]+row < visited[node[0]+row],node[1]+col]

    def orangesRotting(self, grid: List[List[int]]) -> int:
        totalmin = 0
        visitedgrid = [[0]*len(grid[0]) for _ in range(len(grid))]
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # check for the starting node the grid with rotted(2)
                if grid[i][j] == 2:
                    totalmin += 1
                    visitedgrid[i][j] = 2
                    queue.append((i, j, 0))
                    self.bfs(visitedgrid, queue)





Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
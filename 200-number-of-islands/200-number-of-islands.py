class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #遍历矩阵中的每一个点
        num_islands = 0
        visited = set()
        
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == '1' and (row, column) not in visited:
                    self.bfs(grid, row, column, visited)
                    num_islands += 1
        
        return num_islands
    #找到所有相邻的点
    def bfs(self, grid, row, column, visited):
        DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        queue = collections.deque([(row, column)])
        visited.add((row, column))
        
        while queue:
            row, column = queue.popleft()
            for delta_row, delta_column in DIRECTIONS:
                next_row = row + delta_row
                next_column = column + delta_column
                if not self.is_valid(grid, next_row, next_column, visited):
                    continue
                queue.append((next_row, next_column))
                visited.add((next_row, next_column))
        
    #判断一个点是否可以被BFS(没有出界，不是海洋，没被访问过)
    def is_valid(self, grid, row, column, visited):
        #没有出界
        m = len(grid)
        n = len(grid[0])
        if not (0 <= row < m and 0 <= column < n):
            return False
        #没被访问过
        if (row, column) in visited:
            return False
        #海洋还是陆地
        return grid[row][column] == '1'
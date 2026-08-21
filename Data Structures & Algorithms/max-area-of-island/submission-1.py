class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        neighbours = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        m = len(grid)
        n = len(grid[0])

        best = 0
        current = 0
        q = deque()

        for i in range(m):
            for j in range(n):
                current = 0
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0
                    current = 1

                while q:
                    x, y = q.popleft()

                    for neighbour in neighbours:
                        nx = neighbour[0]
                        ny = neighbour[1]
                        
                        newX = x + nx
                        newY = y + ny

                        if newX < 0 or newX >= m:
                            continue
                        if newY < 0 or newY >= n:
                            continue

                        if grid[newX][newY] == 1:
                            q.append((newX, newY))
                            grid[newX][newY] = 0
                            current +=1
                
                best = max(best, current)
        return best

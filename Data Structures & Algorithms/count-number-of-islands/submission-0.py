class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        neighbours = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = 0

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):

                # Found a new island
                if grid[i][j] == '1':
                    res += 1

                    # BFS
                    queue = deque([(i, j)])
                    grid[i][j] = '0'

                    while queue:
                        y, x = queue.popleft()

                        for dy, dx in neighbours:
                            newY = y + dy
                            newX = x + dx

                            # Check boundaries
                            if newY < 0 or newY >= rows:
                                continue
                            if newX < 0 or newX >= cols:
                                continue

                            # Found another part of this island
                            if grid[newY][newX] == '1':
                                grid[newY][newX] = '0'
                                queue.append((newY, newX))

        return res
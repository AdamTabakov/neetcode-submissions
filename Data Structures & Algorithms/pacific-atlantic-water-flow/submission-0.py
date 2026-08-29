class Solution:
    def pacificAtlantic(self, heights):
        n = len(heights)
        m = len(heights[0])

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        pacific = set()
        atlantic = set()

        # Pacific starts
        q = deque()

        for j in range(m):
            q.append((0, j))
            pacific.add((0, j))

        for i in range(n):
            q.append((i, 0))
            pacific.add((i, 0))

        # BFS Pacific
        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if (nx, ny) in pacific:
                    continue

                if heights[nx][ny] >= heights[x][y]:
                    pacific.add((nx, ny))
                    q.append((nx, ny))

        # Atlantic starts
        q = deque()

        for j in range(m):
            q.append((n - 1, j))
            atlantic.add((n - 1, j))

        for i in range(n):
            q.append((i, m - 1))
            atlantic.add((i, m - 1))

        # BFS Atlantic
        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if (nx, ny) in atlantic:
                    continue

                if heights[nx][ny] >= heights[x][y]:
                    atlantic.add((nx, ny))
                    q.append((nx, ny))

        # Cells reachable from both
        return list(pacific & atlantic)
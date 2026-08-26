class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # variable stuff
        q = deque()
        neighbours = [[0,1], [1,0], [-1,0], [0,-1]]
        time = -1

        # add rotten orange placements to q
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i, j])

        # while q exists
        while q:
            time +=1
            for k in range(len(q)):
                cell = q.popleft()
                x, y = cell[0], cell[1]

                for nx, ny in neighbours:
                    newX = nx + x
                    newY = ny + y

                    if newX < 0 or newX >= len(grid) or newY < 0 or newY >= len(grid[0]):
                        continue
                    
                    if grid[newX][newY] == 1:
                        grid[newX][newY] = 2
                        q.append([newX, newY])
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        if time == -1:
            return 0
        
        return time
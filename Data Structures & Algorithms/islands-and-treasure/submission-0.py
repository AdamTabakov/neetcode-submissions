class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        neighbours = [[0,1], [1, 0], [-1, 0], [0, -1]]
        
        # set up bfs
        q = deque()
        distance = 0
        
        # add the treasure chests to the que (On2)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append([i, j])
        
        # expand off of the treasure chests
        while q:
            
            # distance increases by 1 for each iteration
            distance +=1

            # go through each q element
            for i in range(len(q)):
                cell = q.popleft()

                # get the x and y values
                x = cell[0]
                y = cell[1]

                # go through each neighbour
                for neighbour in neighbours:
                    # get new x and y values
                    newX = neighbour[0] + x
                    newY = neighbour[1] + y

                    # make sure it is in the grid
                    if newX < 0 or newX >= len(grid) or newY < 0 or newY >= len(grid[0]):
                        continue
                
                    # if it is inf
                    if grid[newX][newY] == 2147483647:
                        q.append([newX, newY])
                        grid[newX][newY] = distance
        return




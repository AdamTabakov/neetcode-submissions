class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #setup lengths
        rows = len(matrix)
        columns = len(matrix[0])

        # setup pointers
        left = 0
        right = rows * columns - 1

        # binary search
        while left <= right:
            
            #mid
            mid = (left + right) // 2

            # setup row and column
            row = mid // columns
            column = mid % columns

            # if target over
            if matrix[row][column] < target:
                left = mid + 1
            # if target under
            elif matrix[row][column] > target:
                right = mid - 1
            # if in
            else:
                return True

        return False
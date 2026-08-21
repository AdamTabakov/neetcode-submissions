class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # stores all the subsets
        res = []
        # current subset
        subset = []

        # backtrack function
        def backtrack(start):
            
            # add the current subset to the res
            res.append(subset.copy())

            # go through each number starting from start
            for i in range(start, len(nums)):
                # add number to our subset
                subset.append(nums[i])
                # perform backtrack
                backtrack(i + 1)
                # when backtrack done, pop it
                subset.pop()

        backtrack(0)
        return res
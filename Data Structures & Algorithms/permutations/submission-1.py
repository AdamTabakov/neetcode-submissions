class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        current = []
        used = set()

        def backtrack():
            # base case, when it reaches the max length, append to res and return
            if len(current) == len(nums):
                res.append(current.copy())
                return

            # iterate for the length of nums
            for i in range(len(nums)):
                # if the number is currently being used, continue
                if nums[i] in used:
                    continue

                # append the number to current and add it to used
                current.append(nums[i])
                used.add(nums[i])
                # backtrack
                backtrack()
                # when backtracking done, pop it and remove it from used
                current.pop()
                used.remove(nums[i])

        backtrack()
        return res
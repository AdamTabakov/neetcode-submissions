class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        current = []
        used = set()

        def backtrack():
            if len(current) == len(nums):
                res.append(current.copy())
                return

            for i in range(len(nums)):
                if nums[i] in used:
                    continue

                current.append(nums[i])
                used.add(nums[i])

                backtrack()

                current.pop()
                used.remove(nums[i])

        backtrack()
        return res
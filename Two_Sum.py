class Solution:
    def twoSum(self, nums, target: int):
        old = {}
        for f, n in enumerate(nums):
            diff = target - n
            if diff in old:
                return [old[diff],f]
            old[n] = f
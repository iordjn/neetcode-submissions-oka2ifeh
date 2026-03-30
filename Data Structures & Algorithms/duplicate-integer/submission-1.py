class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i, num in enumerate(nums):
            if num in map:
                return True
            map[num] = i
        return False
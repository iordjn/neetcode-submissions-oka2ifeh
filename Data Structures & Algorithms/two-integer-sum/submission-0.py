class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            pair = target - num
            if pair in hash_map:
                return[hash_map[pair], i]
            hash_map[num] = i
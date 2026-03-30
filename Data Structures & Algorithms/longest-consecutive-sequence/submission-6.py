class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        hash_map = defaultdict(int)
        sequences = []
        for num in nums:
            count = 1
            if num - 1 not in nums:
                hash_map[num] += 1
                while num + count in nums:
                    hash_map[num] += 1
                    count +=1
        for value in hash_map.values():
            sequences.append(value)
        if len(sequences) >= 1:
            return max(sequences)
        else:
            return 0

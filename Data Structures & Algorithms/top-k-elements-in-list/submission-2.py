class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)
        count = []
        most_k = []

        for num in nums:
            hash_map[num] += 1

        for value in hash_map.values():
            count.append(value)

        count = sorted(count)
        
        top_k = count[-k:]

        for key, value in hash_map.items():
            if value in top_k:
                most_k.append(key)
        return most_k


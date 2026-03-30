class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = []

        for i, num in enumerate(nums):
            total = 1
            execpt_number = nums.pop(i)
            for j in nums:
                total *= j
            nums.insert(i, execpt_number)
            product.append(total)
        return product

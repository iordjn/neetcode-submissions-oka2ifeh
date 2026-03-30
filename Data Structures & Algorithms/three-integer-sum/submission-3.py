class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)
        for i, num in enumerate(nums):
            left = i +1
            right = len(nums) -1 

            if i > 0 and num == nums[i - 1]:
                continue 

            while left < right:
                found = num + nums[left] + nums[right]
                if found  == 0 and left < right:
                    triplets.append([num, nums[left], nums[right]])
                    left += 1
                    right -=1
                    if nums[left] == nums[left -1] or nums[right] == nums[right +1]:
                        while left < right and nums[left] == nums[left -1]:
                            left +=1
                        while left < right and nums[right] == nums[right +1]:
                            right -=1

                    
                    
                elif found > 0:
                    right -= 1
                else:
                    left += 1
                    
        return triplets
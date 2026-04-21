class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        break_point = nums[left]
        break_point = nums.index(max(nums))

            
        
        if target == nums[break_point]:
            return break_point
        elif nums[break_point] == nums[len(nums)-1]:
            left = 0
            right = len(nums) - 1

        elif target >= nums[left]:
            left =  0
            right = break_point -1 
        else:
            left = break_point + 1
            right = len(nums) -1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1

        

            


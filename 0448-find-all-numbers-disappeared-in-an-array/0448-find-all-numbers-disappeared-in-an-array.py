class Solution(object):
    def findDisappearedNumbers(self, nums):
        for num in nums:
            i = abs(num) - 1
            if nums[i] > 0:
                nums[i] *= -1
        
        return [i + 1 for i, val in enumerate(nums) if val > 0]
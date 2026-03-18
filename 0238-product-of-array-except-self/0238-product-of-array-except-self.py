class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # left pass: answer[i] = product of everything to the LEFT
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # right pass: multiply by product of everything to the RIGHT
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
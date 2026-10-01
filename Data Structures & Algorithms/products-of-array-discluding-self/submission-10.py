class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fix = []
        for i, j in enumerate(nums):
            if i == 0:
                fix.append(1)
            else:
                fix.append(nums[i - 1] * fix[i - 1])
        k = len(nums) - 1
        val = 1
        while k >= 0: 
            if k == len(nums) - 1: 
                val = nums[k]
                k -= 1
                continue
            fix[k] *= val
            val *= nums[k] 
            k -= 1
        return fix
                



        
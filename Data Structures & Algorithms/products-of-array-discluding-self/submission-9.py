class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        m = defaultdict(int)

        for i in nums: 
            m[i] += 1 

        for j, k in enumerate(nums): 
            nums[j] = 1
            for t in m.keys(): 
                if k == t and m[k] > 1: 
                    nums[j] *= (k ** (m[k] - 1))
                elif k != t: 
                    nums[j] *= t ** m[t]
        return nums
                


        
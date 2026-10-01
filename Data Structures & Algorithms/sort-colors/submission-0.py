class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = defaultdict(int)
        for i in nums: 
            m[i] += 1 
        k = 0
        for j in [0, 1, 2]: 
            while m[j] > 0: 
                nums[k] = j 
                m[j] -= 1 
                k += 1 
            
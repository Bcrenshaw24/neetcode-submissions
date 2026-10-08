from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m = defaultdict(int)
        for i in nums: 
            m[i] += 1 
        majority = []
        for k, v in m.items(): 
            if v > len(nums)/3:
                majority.append(k)
        return majority

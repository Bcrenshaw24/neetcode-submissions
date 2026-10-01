class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {} 
        for i, key in enumerate(nums): 
            targ = target - key 
            if targ in need: 
                return [need[targ], i]
            else: 
                need[key] = i
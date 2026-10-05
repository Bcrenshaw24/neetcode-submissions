class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = [] 
        for i in nums: 
            if i != val: 
                temp.append(i) 
        for k in range(len(temp)): 
            nums[k] = temp[k]
        return len(temp)
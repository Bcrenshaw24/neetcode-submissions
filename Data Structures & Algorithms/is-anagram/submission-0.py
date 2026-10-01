class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one = {}    
        two = {} 

        for i in s: 
            if i not in one: 
                one[i] = 1
            else: 
                one[i] += 1
        for j in t: 
            if j not in two: 
                two[j] = 1
            else: 
                two[j] += 1 
        return one == two
        
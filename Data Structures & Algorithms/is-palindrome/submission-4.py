class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = [] 
        for i in s: 
            if i in [" ", ",", "?", "!", "'", ".", ":"]: 
                continue 
            stack.append(i.lower()) 
    
        for j in s: 
            if j in [" ", ",", "?", "!", "'", ".", ":"]:
                continue 
            if j.lower() != stack[-1]: 
                return False 
            stack.pop() 
        return True

            
        
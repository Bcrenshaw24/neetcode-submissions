class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """ 
        Sort the array: O(NlogN + N + L)
        sorting each: O(m * nlogn)
        """
        s = defaultdict(list)
        for i in strs: 
            sortS = ''.join(sorted(i)) 
            s[sortS].append(i) 
        return list(s.values())
       
            


            
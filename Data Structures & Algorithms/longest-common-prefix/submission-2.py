class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        pre = ""
        for i in range(min(len(strs[0]), len(strs[-1]))): 
            if strs[0][i] == strs[-1][i]: 
                print(strs[0][i])
                pre += strs[0][i]
            else: 
                return pre
        if not pre: 
            return ""
        return pre

        
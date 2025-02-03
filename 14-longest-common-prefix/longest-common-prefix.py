class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        hash={}
        for char in strs:
            n = len(char)
            for i in range(n):
                if char[:i+1] in hash:
                    hash[char[:i+1]]+=1
                
                else:
                    hash[char[:i+1]]=1
        maxx=''
        for s,count in hash.items():
            if count==len(strs) and len(maxx)<len(s):
                maxx=s

        return maxx 
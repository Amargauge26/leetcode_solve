class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''

        f = {}

        n = len(s)

        for i in range(n):
            if s[i] in f:
                f[s[i]]+=1
            
            else:
                f[s[i]]=1
        
        ss = sorted(f.items(),key = lambda x:(-x[1],x[0]))

        for k,v in ss:
                ans+=k*v
        

        return ans



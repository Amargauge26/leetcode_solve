class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""

        f ={}

        for char in s:
            if char in f:
                f[char]+=1
            
            else:
                f[char]=1



        LL = sorted(f.items(),key=lambda x:(-x[1],x[0]))

        for k,v in LL:
            ans+=k*v

        return ans
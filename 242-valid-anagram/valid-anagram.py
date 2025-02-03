from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        ss= Counter(s)
        tt= Counter(t)
        if len(s)!=len(t):
            return False

        for k,v in ss.items():
            if k not in tt:
                return False
            else:
                if v!=tt[k]:
                    return False
                
                else:
                    continue
        
        return True
        
        
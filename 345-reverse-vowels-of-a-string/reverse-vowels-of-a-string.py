class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        j = len(s)-1
        h =['a', 'e', 'i', 'o','u',"A","E","I","O","U"]
        ss=list(s)
        while i<j:
            if ss[i] not in h and ss[j] in h:
                i+=1
            elif ss[i] in h and ss[j] not in h:
                j-=1
            elif ss[i] not in h and ss[j] not in h:
                i+=1
                j-=1
            else:
                ss[i],ss[j]=ss[j],ss[i]
                i+=1
                j-=1
            
        return "".join(ss)
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = prices[0]
        maxi=0
        for i in range(1,len(prices)):
            if s>prices[i]:
                s=prices[i]
            else:
                maxi=max(maxi,prices[i]-s)
        return maxi


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        arr=sorted(intervals, key=lambda x: x[0])

        ans = [arr[0]]
        n = len(intervals)
        for i in range(1,n):

            last = ans[-1]

            if arr[i][0]<=last[1]:
                last[1]=max(last[1],arr[i][1])
            else:
                ans.append(arr[i])
        return ans
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h = Counter(arr)
        occurrences = h.values()
        return len(occurrences) == len(set(occurrences))
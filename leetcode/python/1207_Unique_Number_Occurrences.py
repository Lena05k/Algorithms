class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}

        for item in arr:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1

        return len(counts.values()) == len(set(counts.values()))

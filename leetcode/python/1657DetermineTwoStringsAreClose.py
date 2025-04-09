class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        counts1 = {}

        for item in word1:
            if item in counts1:
                counts1[item] += 1
            else:
                counts1[item] = 1

        counts2 = {}

        for item in word2:
            if item in counts2:
                counts2[item] += 1
            else:
                counts2[item] = 1

        return sorted(counts1.values()) == sorted(counts2.values())
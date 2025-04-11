class Solution:
    def removeStars(self, s: str) -> str:
        stask = []

        for char in s:
            if char == '*':
                stask.pop()
            else:
                stask.append(char)
        return ''.join(stask)
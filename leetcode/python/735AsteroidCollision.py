class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stask = []

        for asteroid in asteroids:
            while stask and asteroid < 0 < stask[-1]:
                if stask[-1] < -asteroid:
                    stask.pop()
                    continue
                elif stask[-1] == -asteroid:
                    stask.pop()
                    break
            else:
                stask.append(asteroid)
        return stask



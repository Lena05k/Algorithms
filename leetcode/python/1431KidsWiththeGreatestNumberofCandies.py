class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxCandies = max(candies)

        for candy in candies:
            result.append(candy + extraCandies >= maxCandies)
        return result
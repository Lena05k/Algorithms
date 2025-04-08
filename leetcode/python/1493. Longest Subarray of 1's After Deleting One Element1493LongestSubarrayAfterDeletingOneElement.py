class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        max_len = 0
        zeros = 0
        k = 1

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1


            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len - 1
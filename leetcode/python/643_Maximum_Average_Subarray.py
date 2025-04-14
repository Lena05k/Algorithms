


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # шаг 1: считаем сумму первых k чисел, допустим k = 3, а массив nums = [1, 3, 5, 2, 8]
        # окно - [1, 3, 5]
        current_sum = sum(nums[:k]) # 1 + 3 + 5 = 9
        max_sum = current_sum

        for i in range(k, len(nums)):
            # шаг 2: двигаем "окно" по массиву, было [1, 3, 5] → стало [3, 5, 2] вычитаем 1, прибавляем 2
            current_sum = current_sum - nums[i - k] + nums[i] # i = k = от 3
            # шаг 3: следим за max
            max_sum = max(max_sum, current_sum)
        # шаг 4: получить среднее max число
        return max_sum / k

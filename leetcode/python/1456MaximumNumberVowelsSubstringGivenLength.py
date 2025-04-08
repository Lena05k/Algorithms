class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = { 'a', 'e', 'i', 'o', 'u' }
        count = 0

        # шаг 1: посчитать все гласные в первых k символах
        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count

        # шаг 2: двигаем "окно" по строке по одному символу вправо
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count -= 1 # тот, кто ушёл — гласный? вычитаем
            if s[i] in vowels:
                count += 1 # тот, кто пришёл — гласный? прибавляем

            max_count = max(max_count, count)

        return max_count
# s = "abciiidef"
# k = 3

#"abc"    → count = 1
# "bci"   → count = 1
#  "cii"  → count = 2
#   "iii" → count = 3 MAX
#    "iid"→ count = 2
#     "ide"→ count = 2
#      "def"→ count = 1
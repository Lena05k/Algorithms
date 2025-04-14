class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ''
        for char in s:
          if char.isdigit():
            current_num = current_num * 10 + int(char);
          elif char == '[':
            stack.append((current_str, current_num))
            current_str = ''
            current_num = 0
          elif char == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
          else:
            current_str += char
        return current_str

# def decodeString(s):
#     stack = []
#     current_num = 0
#     current_str = ''
#
#     print(f"\nИсходная строка: {s}\n")
#
#     for i, char in enumerate(s):
#         print(f"\nШаг {i}: Текущий символ = '{char}'")
#         print(f"До обработки: current_num = {current_num}, current_str = '{current_str}', stack = {stack}")
#
#         if char.isdigit():
#             current_num = current_num * 10 + int(char)
#             print(f"Найдена цифра: current_num обновлено до {current_num}")
#
#         elif char == '[':
#             stack.append((current_str, current_num))
#             print(f"Найдено '[': Добавили в stack = {stack}")
#             current_str = ''
#             current_num = 0
#             print(f"Сбросили current_str и current_num")
#
#         elif char == ']':
#             prev_str, num = stack.pop()
#             print(f"Найдено ']': Извлекли из stack: prev_str = '{prev_str}', num = {num}")
#             current_str = prev_str + current_str * num
#             print(f"Обновили current_str = '{prev_str}' + '{current_str}' * {num} = '{current_str}'")
#
#         else:
#             current_str += char
#             print(f"Найдена буква: current_str = '{current_str}'")
#
#         print(f"После обработки: current_num = {current_num}, current_str = '{current_str}', stack = {stack}")
#
#     print("\nРезультат:")
#     return current_str
#
#
# print(decodeString("3[a]2[bc]"))
# Сложность: O(N²) в худшем случае (например, для вырожденного дерева)
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0  # Счётчик подходящих путей

        # Эта функция считает пути, начинающиеся в данном узле
        def dfs(node, current_sum): # для каждого узла считает все пути, начинающиеся в нём и дающие в сумме targetSum
            if not node:
                return  # Базовый случай: если узла нет, выходим

            current_sum += node.val  # Обновляем текущую сумму
            if current_sum == targetSum:
                self.count += 1  # Нашли подходящий путь

            # Рекурсивно проверяем левое и правое поддеревья
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

        # Эта функция обходит все узлы дерева
        def traverse(node): # вызывает dfs для каждого узла дерева, обеспечивая проверку всех возможных стартовых точек.
            if not node:
                return  # Базовый случай: пустое дерево

            dfs(node, 0)  # Запускаем dfs для текущего узла (начинаем новый путь)
            traverse(node.left)  # Рекурсивно обходим левое поддерево
            traverse(node.right)  # Рекурсивно обходим правое поддерево

        traverse(root)  # Начинаем обход с корня
        return self.count  # Возвращаем итоговое количество путей

# ВТОРОЙ СПОСОБ
# Сложность: O(N) — каждый узел посещается один раз.
# Память: O(N) — для хранения префиксных сумм (в худшем случае, например, для вырожденного дерева).
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        from collections import defaultdict
        self.count = 0  # Счётчик подходящих путей
        prefix_sums = defaultdict(int)  # Хранит количество встреч каждой префиксной суммы
        prefix_sums[0] = 1  # Базовый случай: сумма 0 встречается 1 раз (пустой путь)

        def dfs(node, current_sum):
            if not node:
                return  # Базовый случай: пустой узел

            current_sum += node.val  # Обновляем текущую сумму пути
            # Если (current_sum - targetSum) есть в prefix_sums, значит, есть подпуть с суммой targetSum
            self.count += prefix_sums.get(current_sum - targetSum, 0)

            # Добавляем текущую сумму в словарь для дочерних узлов
            prefix_sums[current_sum] += 1
            dfs(node.left, current_sum)  # Рекурсивно проверяем левое поддерево
            dfs(node.right, current_sum)  # Рекурсивно проверяем правое поддерево
            # Возвращаемся назад: убираем текущую сумму, чтобы не влиять на другие ветви
            prefix_sums[current_sum] -= 1

        dfs(root, 0)  # Начинаем обход с корня (текущая сумма = 0)
        return self.count


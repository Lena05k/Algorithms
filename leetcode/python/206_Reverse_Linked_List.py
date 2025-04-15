# Дано: Голова односвязного списка
# Нужно: Развернуть список и вернуть новую голову
# Пример:
# Ввод: 1->2->3->4->5->None
# Вывод: 5->4->3->2->1->None
#
# Решение:
# Итеративный метод с тремя указателями:
# 1. Сохраняем следующий узел (next_node)
# 2. Разворачиваем ссылку текущего узла (current.next = prev)
# 3. Сдвигаем указатели (prev и current) вперед
# Сложность: O(n) по времени, O(1) по памяти

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
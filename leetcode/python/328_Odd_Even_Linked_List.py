class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Если список пуст или содержит только 1 элемент
        if not head or not head.next:
            return head

        # Инициализация указателей:
        # odd_head - начало нечётного списка (1-й узел)
        # odd_tail - конец нечётного списка
        # even_head - начало чётного списка (2-й узел)
        # even_tail - конец чётного списка
        odd_head = odd_tail = head
        even_head = even_tail = head.next

        # Исходный список: [1] → [2] → [3] → [4] → None
        # head = [1](нечётная позиция)
        # head.next = [2](чётная позиция)

        # current начинаем с 3-го узла (если есть)
        current = even_head.next # [2].next = [3] → это как раз 3-й узел
        index = 3  # счётчик позиций

        while current:
            if index % 2 == 1:  # нечётная позиция
                odd_tail.next = current
                odd_tail = odd_tail.next
            else:  # чётная позиция
                even_tail.next = current
                even_tail = even_tail.next

            current = current.next
            index += 1

        # Соединяем нечётный список с чётным
        odd_tail.next = even_head
        # Обрываем конец чётного списка
        even_tail.next = None

        return odd_head
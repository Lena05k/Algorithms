def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # Краевой случай: пустой список или 1 элемент
    if not head or not head.next:
        return None

    # Инициализация указателей
    slow = head
    fast = head
    prev = None  # Будет хранить узел перед slow

    # Двигаем fast в 2 раза быстрее slow
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Удаляем middle-узел (prev.next теперь указывает на slow.next)
    prev.next = slow.next

    return head
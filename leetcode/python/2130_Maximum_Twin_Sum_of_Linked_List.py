class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Шаг 1: Находим середину списка с помощью быстрого и медленного указателя
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Шаг 2: Разворачиваем вторую половину списка
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Шаг 3: Идем с двух концов к середине, вычисляя суммы
        max_sum = 0
        left, right = head, prev
        while right:
            current_sum = left.val + right.val
            if current_sum > max_sum:
                max_sum = current_sum
            left = left.next
            right = right.next

        return max_sum
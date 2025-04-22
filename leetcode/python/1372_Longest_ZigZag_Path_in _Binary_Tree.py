class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, 'left', 0), (root, 'right', 0)]
        max_len = 0

        while stack:
            node, direction, length = stack.pop()
            max_len = max(max_len, length)

            if direction == 'left':
                if node.left:
                    stack.append((node.left, 'right', length + 1))
                if node.right:
                    stack.append((node.right, 'left', 1))
            else:
                if node.right:
                    stack.append((node.right, 'left', length + 1))
                if node.left:
                    stack.append((node.left, 'right', 1))

        return max_len

# ВТОРОЙ СПОСОБ
from collections import deque
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_steps = 0
        queue = deque([(root, True, 0), (root, False, 0)])

        while queue:
            node, go_left, steps = queue.popleft()
            max_steps = max(max_steps, steps)

            if go_left:
                if node.left:
                    queue.append((node.left, False, steps + 1))
                if node.right:
                    queue.append((node.right, True, 1))
            else:
                if node.right:
                    queue.append((node.right, True, steps + 1))
                if node.left:
                    queue.append((node.left, False, 1))

        return max_steps
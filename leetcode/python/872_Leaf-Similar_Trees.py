# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(root):
            if not root:
                return []

            stack = [root]
            leaves = []

            while stack:
                node = stack.pop()

                if not node.left and not node.right:
                    leaves.append(node.val)

                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

            return leaves

        leaves1 = get_leaves(root1)
        leaves2 = get_leaves(root2)

        return leaves1 == leaves2
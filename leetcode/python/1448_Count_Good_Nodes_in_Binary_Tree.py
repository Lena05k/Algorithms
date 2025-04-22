class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0

        def dfs(node, current_max):
            if not node:
                return

            if node.val >= current_max:
                self.good_nodes += 1
                current_max = node.val

            dfs(node.left, current_max)
            dfs(node.right, current_max)

        dfs(root, root.val)
        return self.good_nodes


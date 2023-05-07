from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_nodes_at_level(root, level):
    if not root:
        return 0

    q = deque([(root, 0)])
    count = 0

    while q:
        node, current_level = q.popleft()

        if current_level == level:
            count += 1

        if node.left:
            q.append((node.left, current_level + 1))

        if node.right:
            q.append((node.right, current_level + 1))

    return count

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


print(count_nodes_at_level(root, 2)) 
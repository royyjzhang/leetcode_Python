from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Node:
    def __init__(self, treenode, level):
        self.treenode = treenode
        self.level = level

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue = deque([])
        result = []
        now = Node(root, 0)
        total = 0
        count = 0
        current_level = 0
        queue.append(now)
        while queue:
            now = queue.popleft()
            if now.level > current_level:
                result.append(total / count)
                total = now.treenode.val
                count = 1
                current_level = now.level
            else:
                total += now.treenode.val
                count += 1
            if now.treenode.left:
                queue.append(Node(now.treenode.left, current_level + 1))
            if now.treenode.right:
                queue.append(Node(now.treenode.right, current_level + 1))
        result.append(total / count)
        return result
   
def main():
    solution = Solution()
    root = TreeNode(3)
    p = TreeNode(9)
    root.left = p
    p = TreeNode(20)
    root.right = p
    p = TreeNode(15)
    root.right.left = p
    p = TreeNode(7)
    root.right.right = p
    print(solution.averageOfLevels(root))

if __name__=="__main__":
    main()
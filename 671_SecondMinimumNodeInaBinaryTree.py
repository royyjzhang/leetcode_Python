from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = deque([])
        result = float('inf')
        mininum = root.val
        queue.append(root)
        while queue:
            now = queue.popleft()
            if mininum < now.val < result:
                result = now.val
            if now.left:
                queue.append(now.left)
                queue.append(now.right)
        if result == float('inf'):
            return -1
        else:
            return result

def main():
    solution = Solution()
    root = TreeNode(2)
    p = TreeNode(2)
    root.left = p
    p = TreeNode(5)
    root.right = p
    p = TreeNode(5)
    root.right.left = p
    p = TreeNode(7)
    root.right.right = p
    print(solution.findSecondMinimumValue(root))

if __name__=="__main__":
    main()
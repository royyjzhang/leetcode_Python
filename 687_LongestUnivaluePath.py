# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.result = 0
        self.dfs(root)
        return self.result

    def dfs(self, root):
        if root.left:
            leftLength = self.dfs(root.left)
        else:
            leftLength = 0
        if root.right:
            rightLength = self.dfs(root.right)
        else:
            rightLength = 0

        if root.left and root.val == root.left.val:
            leftResult = leftLength + 1
        else:
            leftResult = 0
        if root.right and root.val == root.right.val:
            rightResult = rightLength + 1
        else:
            rightResult = 0

        if self.result < leftResult + rightResult:
            self.result = leftResult + rightResult

        return max(leftResult, rightResult)

def main():
    solution = Solution()
    root = TreeNode(1)
    p = TreeNode(4)
    root.left = p
    p = TreeNode(4)
    root.left.left = p
    p = TreeNode(4)
    root.left.right = p
    p = TreeNode(5)
    root.right = p
    p = TreeNode(5)
    root.right.right = p
    print(solution.longestUnivaluePath(root))

if __name__=="__main__":
    main()
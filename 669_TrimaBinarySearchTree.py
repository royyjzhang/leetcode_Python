# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if (root == None):
            return root
        if (root.val < L):
            return self.trimBST(root.right, L, R)
        if (root.val > R):
            return self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root

def printTree(root):
    if (root == None):
        return
    print(root.val)
    printTree(root.left)
    printTree(root.right)

def main():
    solution = Solution()
    L = 1
    R = 3
    root = TreeNode(3)
    p = TreeNode(0)
    root.left = p
    p = TreeNode(4)
    root.right = p
    p = TreeNode(2)
    root.left.right = p
    p = TreeNode(1)
    root.left.right.left = p
    print("Before")
    printTree(root)
    print("After")
    printTree(solution.trimBST(root, L, R))

if __name__=="__main__":
    main()
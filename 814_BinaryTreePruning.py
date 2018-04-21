# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNodes(self, root):
        if (root == None):
            return None
        if (self.deleteNodes(root.left) == None):
            root.left = None
        if (self.deleteNodes(root.right) == None):
            root.right = None
        if ((root.left == None) and (root.right == None) and (root.val == 0)):
            return None
        else:
            return root

    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if (root == None):
            return None
        self.deleteNodes(root)
        return root

def tranverse_tree(root):
    if not root:
        return
    print(root.val)
    tranverse_tree(root.left)
    tranverse_tree(root.right)

def main():
    solution = Solution()
    root = TreeNode(1)
    p = TreeNode(0)
    root.right = p
    p = TreeNode(0)
    root.right.left = p
    p = TreeNode(1)
    root.right.right = p
    new_root = solution.pruneTree(root)
    tranverse_tree(new_root)

if __name__ == "__main__":
    main()
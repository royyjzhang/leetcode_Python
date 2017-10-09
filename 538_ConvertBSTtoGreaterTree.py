# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.sum = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.convert(root)
        return root

    def convert(self, root):
        if not root:
            return
        self.convert(root.right)
        root.val += self.sum
        self.sum = root.val
        self.convert(root.left)

def printTree(root):
    if (root == None):
        return
    print(root.val)
    printTree(root.left)
    printTree(root.right)
        
def main():
    solution = Solution()
    root = TreeNode(3)
    p = TreeNode(9)
    root.left = p
    p = TreeNode(20)
    root.right = p
    p = TreeNode(15)
    root.right.left = p
    p = TreeNode(23)
    root.right.right = p
    print("Before")
    printTree(root)
    print("After")
    printTree(solution.convertBST(root))

if __name__=="__main__":
    main()
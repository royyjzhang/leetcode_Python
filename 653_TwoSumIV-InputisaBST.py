# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        return self.dfs(root, root, k)

    def dfs(self, current, root, k):
        if not current:
            return False
        return self.search(root, current, k - current.val) or self.dfs(current.left, root, k) or self.dfs(current.right, root, k)
    
    def search(self, root, current, k):
         if not root:
             return False
         return ((root.val == k) and (root != current)) or ((root.val < k) and self.search(root.right, current, k)) or ((root.val > k) and self.search(root.left, current, k))
        
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
    print(solution.findTarget(root, 13))

if __name__=="__main__":
    main()
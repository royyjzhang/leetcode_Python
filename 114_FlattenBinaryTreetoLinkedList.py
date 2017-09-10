# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#因为无法达到引用传递效果，不可以不return
class Solution(object):
	def flat(self,root):
		now=root
		while (now!=None):
			if (now.left!=None):
				temp=now.left
				while (temp.right!=None):
					temp=temp.right
				temp.right=now.right
				now.right=temp
				now.left=None
			now=now.right
		return root
	def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if (root==None):
        	return
        root=self.flat(root)

solution=Solution()
root=TreeNode(1)
p=TreeNode(2)
root.left=p
p=TreeNode(3)
root.left.left=p
p=TreeNode(4)
root.left.right=p
p=TreeNode(5)
root.right=p
p=TreeNode(6)
root.right.right=p
solution.flatten(root)
p=root
while (p!=None):
	print p.val
	p=p.right
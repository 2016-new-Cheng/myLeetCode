# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.core(1, n)
        
    def core(self, start, end):
        res = []
        if start > end:
            res.append(None)
            return res
        for i in xrange(start, end + 1):
            left = self.core(start, i - 1)
            right = self.core(i + 1, end)
            for lnode in left:
                for rnode in right:
                    root = TreeNode(i)
                    root.left = lnode
                    root.right = rnode
                    res.append(root)
                    
        return res

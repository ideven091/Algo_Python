from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def insert(self, root: TreeNode, data):
        if root is None:
            root = TreeNode(val=data)
        elif data < root.val:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def isBST(self, root, minimum, maximum):
        if root is None:
            return True
        return (root.val > minimum and root.val < maximum) and self.isBST(root.left, minimum, root.val) and self.isBST(
            root.right, root.val, maximum)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        minimum = -21474836488
        maximum = 21474836477
        return self.isBST(root, minimum, maximum)

    def inOrder(self, root):
        if root is not None:
            self.inOrder(root.left)
            print(root.val, end=" ")
            self.inOrder(root.right)
            
    def postOrder(self,root):
        if root is not None:
            print(root.val,end=' ')
            self.postOrder(root.left)
            self.postOrder(root.right)
            


class Solution:
    if __name__ == "__main__":
        tree = Tree()
        root = TreeNode(1)
        tree.insert(root, 2)
        tree.insert(root, 7)
        tree.insert(root, 6)
        tree.insert(root, 5)
        tree.inOrder(root)
        print()
        tree.postOrder(root)

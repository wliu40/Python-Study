# -*- coding: cp936 -*-

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)
    
class BSTree():
    def __init__(self):
        self.root = None        
        self.flag = False
        
    def preorderTrav(self):
        self.preorderTravHelper(self.root)
        
    def preorderTravHelper(self, startNode):
        if startNode != None:
            print startNode, " ",
            self.preorderTravHelper(startNode.left)
            self.preorderTravHelper(startNode.right)
            
    def insert_Iterative(self, val):
        newNode = Node(val)
        if self.root == None:            
            self.root = newNode
            return
        curNode = self.root
        while True:
            if val < curNode.val:
                if curNode.left != None:
                    curNode = curNode.left
                else:
                    curNode.left = newNode                    
                    break
            else:
                if curNode.right != None:
                    curNode = curNode.right
                else:
                    curNode.right = newNode
                    break
    def convert(self, l):
        for i in l:
            self.insert_Iterative(i)
            
    def getRoot(self):
        return self.root

    
    def DFS_Recur(self, target):   
        stack = []
        flag = [0]
        self.DFS_Recur_Helper(self.root, target, stack, flag)
        if flag[0] == 1:
            print '到该node的路径是： ',
            print stack
        else:
            print 'node not found'
        
    def DFS_Recur_Helper(self, _root, target, stack, flag):   
        if _root == None or flag[0] == 1:
            return
        stack.append(_root.val)
        if _root.val == target:
            flag[0] = 1
            return        
        self.DFS_Recur_Helper(_root.left, target, stack, flag)
        self.DFS_Recur_Helper(_root.right, target, stack, flag)
        if stack[-1] != target:
            stack.pop(-1)
            
    def DFS_Iter(self, target):
        stack = [self.root]
        while len(stack) > 0:
            curNode = stack.pop(-1)
            if curNode.val == target:
                return True
            else:
                if curNode.right != None:
                    stack.append(curNode.right)
                if curNode.left != None:
                    stack.append(curNode.left)
        return False
    def BFS_Iter(self):
        queue = [self.root]
        while len(queue) > 0:
            curNode = queue.pop(0)
            print curNode.val, ' ',
            if curNode.left:
                queue.append(curNode.left)
            if curNode.right:
                queue.append(curNode.right)
    def findHeight(self):
        return self.findHeightHelper(self.root)
    def findHeightHelper(self, _root):
        if not _root:
            return 0
        leftHeight = self.findHeightHelper(_root.left)
        rightHeight = self.findHeightHelper(_root.right)
        if(leftHeight > rightHeight):
            return leftHeight+1
        else:
            return rightHeight+1
        
           

def main():
    intList = []
    while True:
        val = raw_input('please input a integer array(q to quit): ')
        if val == 'q' or val == 'Q':
            break
        intList.append(int(val))

    print 'intList = ',
    print intList
    
    print '把intList转为Binary Search Tree: ...'
    bt = BSTree()
    bt.convert(intList)
    
    print '先序遍历该Binary Search Tree: '
    bt.preorderTrav()
    print ''

    while True:
        target = raw_input('please input the value to find(q to quit): ')
        if target == 'q' or target == 'Q':
            break

        bt.DFS_Recur(int(target))

    print '层次遍历(BFS)该树： ',
    bt.BFS_Iter()
    print "\nthe height of the tree: ",
    print bt.findHeight()


if __name__ == '__main__':

    main()

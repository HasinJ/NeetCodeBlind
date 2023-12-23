from treenode import *

def test(root, q, p):
    if root == None:
        return [False, False]

    left = test(root.left, q, p)
    right = test(root.right, q, p)

    res = [False, False]

    if len(left) == 1: return left
    if len(right) == 1: return right

    if left[0] or right[0]:
        res[0] = True

    if left[1] or right[1]:
        res[1] = True

    if root.val == p.val:
        res[0] = True

    if root.val == q.val:
        res[1] = True

    if res == [True, True]: return [root]

    return res

# print(test(root, q, p))


list = [6,2,8,0,4,7,9,None,None,3,5]
root = createBTree(list, 0)
root.display()
p = TreeNode(5)
q = TreeNode(3)

print( test(root, q, p)[0].val )


from collections import defaultdict
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def height(root):
    if root == None:
        return 0
    l = height(root.left)
    r = height(root.right)

    return 1 + max(l, r)

def level_order(root, index, level, l):
    if root == None:
        return
    if level == 1:
        l.append(root.info)
        return 
    level_order(root.left, index, level-1, l)
    level_order(root.right, index, level-1, l)

def vertical_traversal(root, index, d, l):
    if root == None:
        return 
    t = l.index(root.info)
    d[index].append((t, root.info))    
    vertical_traversal(root.left, index-1, d, l)
    vertical_traversal(root.right, index+1, d, l)

def search(item, l):

    res = []
    for i in item:
        t = l.index(i)
        res.append((t, i))
        
    return res

def topView(root):
    h = height(root)
    d = defaultdict(list)
    l = []

    for i in range(1, h+1):
        level_order(root, i, i, l)

    vertical_traversal(root, 0, d, l)

    s = sorted(d.items())
    res = []
    for k, item in s:
        if len(item) == 1:
            res.append(item[0][1])
        else:
            item.sort()
            res.append(item[0][1])


    print(" ".join(map(str, res)))






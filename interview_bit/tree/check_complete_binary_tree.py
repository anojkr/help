# Python program to check if a binary tree complete or not 
  
# Tree node structure 
class Node: 
  
    # Contructor to create a new node 
    def __init__(self, key): 
        self.key = key 
        self.left = None 
        self.right = None 
  
  
# This function counts the number of nodes in a binary tree 
def countNodes(root): 
    if root is None: 
        return 0 
    return (1+ countNodes(root.left) + countNodes(root.right)) 
  
# This function checks if binary tree is complete or not 
def isComplete(root, index, number_nodes): 
      
    # An empty is complete 
    if root is None: 
        return True
      
    # If index assigned to current nodes is more than 
    # number of nodes in tree, then tree is not complete 
    if index >= number_nodes : 
        return False
      
    # Recur for left and right subtress 
    return (isComplete(root.left , 2*index+1 , number_nodes) 
        and isComplete(root.right, 2*index+2, number_nodes) 
          ) 
  
"""
Given a binary tree, find its height.

Example 1:

Input:
     1
    /  \
   2    3
Output: 2
Example 2:

Input:
  2
   \
    1
   /
 3
Output: 3   
Your Task:
You don't need to read input or print anything. Your task is to complete the function height() which takes root node of the tree as input parameter and returns an integer denoting the height of the tree. If the tree is empty, return 0. 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= Number of nodes <= 105
1 <= Data of a node <= 109

"""

class Solution:
    # Function to find the height of a binary tree.
    def height(self, root):
        if root is None:
            return 0
        else:
            # Compute the height of each subtree
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            
            # Use the larger one
            return max(left_height, right_height) + 1


# { 
# Driver Code Starts
# Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == "N":
        return None
        
    # Creating list of strings from input 
    # string after splitting by space
    ip = list(map(str, s.split()))
    
    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()
    
    # Push the root to the queue
    q.append(root)                            
    size = size + 1 
    
    # Starting from the second element
    i = 1                                       
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1
        
        # Get the current node's value from the string
        currVal = ip[i]
        
        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if i >= len(ip):
            break
        currVal = ip[i]
        
        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        ob = Solution()
        print(ob.height(root))

# } Driver Code Ends

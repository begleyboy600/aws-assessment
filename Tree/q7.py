"""
The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two end nodes. The diagram below shows two trees each with diameter nine, the leaves that form the ends of the longest path are shaded (note that there is more than one path in each tree of length nine, but no path longer than nine nodes). 



Example 1:

Input:
       1
     /  \
    2    3
Output: 3
Example 2:

Input:
         10
        /   \
      20    30
    /   \ 
   40   60
Output: 4
Your Task:
You need to complete the function diameter() that takes root as parameter and returns the diameter.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 <= Number of nodes <= 10000
1 <= Data of a node <= 1000
"""


class Solution:
    
    # Function to return the diameter of a Binary Tree.
    def diameter(self, root):
        # Initialize the diameter
        self.max_diameter = 0
        
        def height(node):
            # Base case: An empty tree has height 0
            if not node:
                return 0
            
            # Recursively get the height of the left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update the diameter if the path through the current node is longer
            self.max_diameter = max(self.max_diameter, left_height + right_height + 1)
            
            # Return the height of the current node
            return max(left_height, right_height) + 1
        
        # Start the recursive height calculation
        height(root)
        
        # The diameter is stored in max_diameter
        return self.max_diameter

# { 
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by Sudarshan Sharma
from collections import deque
import sys
sys.setrecursionlimit(50000)
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
        k = Solution().diameter(root)
        print(k)

# } Driver Code Ends

"""
Given an array of strings arr[] of size N, find if there exists 2 strings arr[i] and arr[j] such that arr[i]+arr[j] is a palindrome i.e the concatenation of string arr[i] and arr[j] results into a palindrome.


Example 1:

Input:
N = 6
arr[] = {"geekf", "geeks", "or","keeg", "abc", 
          "bc"}
Output: 1 
Explanation: There is a pair "geekf"
and "keeg".
Example 2:

Input:
N = 5
arr[] = {"abc", "xyxcba", "geekst", "or", "bc"}
Output: 1
Explanation: There is a pair "abc"
and "xyxcba".

Your Task:  
You don't need to read input or print anything. Your task is to complete the function palindromepair() which takes the array arr[], its size N and returns true if palindrome pair exists and returns false otherwise.
The driver code itself prints 1 if returned value is true and prints 0 if returned value is false.
 

Expected Time Complexity: O(N*l2) where l = length of longest string in arr[]
Expected Auxiliary Space: O(N*l2) where l = length of longest string in arr[]
 

Constraints:
1 ≤ N ≤ 2*104
1 ≤ |arr[i]| ≤ 10
"""

class Solution:
    def palindromepair(self, N, arr):
        def is_palindrome(s):
            return s == s[::-1]
        
        seen = set()
        
        for s in arr:
            if s in seen:
                continue
            
            n = len(s)
            
            # Check all possible pairs (s, prefix) and (suffix, s)
            for i in range(n):
                prefix = s[:i]
                suffix = s[i:]
                
                if is_palindrome(prefix + s):
                    return True
                if is_palindrome(s + suffix):
                    return True
            
            seen.add(s)
        
        return False


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=[]
        for i in range(N):
            s = input()
            arr.append(s)
        
        ob = Solution()
        print(ob.palindromepair(N,arr))
# } Driver Code Ends
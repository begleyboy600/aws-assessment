"""
Given a string s, the task is to check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. 

Example 1:

Input: s = "ababab"
Output: 1
Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, act and tac are an anagram of each other. Strings a and b can only contain lower case alphabets.

Note:-

If the strings are anagrams you have to return True or else return False

|s| represents the length of string s.


Example 1:

Input:a = geeksforgeeks, b = forgeeksgeeks
Output: YES
Explanation: Both the string have same characters with
        same frequency. So, both are anagrams.
Example 2:

Input:a = allergy, b = allergic
Output: NO
Explanation: Characters in both the strings are 
        not same, so they are not anagrams.
Your Task:
You don't need to read input or print anything. Your task is to complete the function isAnagram() which takes the string a and string b as input parameter and check if the two strings are an anagram of each other. The function returns true if the strings are anagram else it returns false.

Expected Time Complexity:O(|a|+|b|).
Expected Auxiliary Space: O(Number of distinct characters).

Constraints:
1 ≤ |a|,|b| ≤ 105
"""

class Solution: 
    def isAnagram(self, a, b):
        # If the lengths of the two strings are different, they can't be anagrams
        if len(a) != len(b):
            return False
        
        # Create frequency dictionaries for both strings
        freq_a = {}
        freq_b = {}

        # Count the frequency of each character in string a
        for char in a:
            if char in freq_a:
                freq_a[char] += 1
            else:
                freq_a[char] = 1
        
        # Count the frequency of each character in string b
        for char in b:
            if char in freq_b:
                freq_b[char] += 1
            else:
                freq_b[char] = 1

        # Compare the frequency dictionaries
        return freq_a == freq_b
    

# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = map(str, input().strip().split())
        if Solution().isAnagram(a, b):
            print("YES")
        else:
            print("NO")
# Driver Code Ends
'''
Closest Strings         https://www.geeksforgeeks.org/problems/closest-strings0611/1?page=1&difficulty=Easy&sortBy=submissions
Difficulty: Easy

Given a list of words followed by two words, the task to find the minimum distance between the given two words in the list of words

Example 1:
Input:
S = { "the", "quick", "brown", "fox", 
     "quick"}
word1 = "the"
word2 = "fox"
Output: 3
Explanation: Minimum distance between the 
words "the" and "fox" is 3

Example 2:
Input:
S = {"geeks", "for", "geeks", "contribute", 
     "practice"}
word1 = "geeks"
word2 = "practice"
Output: 2
Explanation: Minimum distance between the
words "geeks" and "practice" is 2

Your Task:  
You don't need to read input or print anything. Your task is to complete the function

shortestDistance() which list of words, two strings as inputs and returns the minimum distance between two words

Expected Time Complexity: O(N*|S|)
Expected Auxiliary Space: O(1)

Constraints:
Sum of lengths of words ≤ 105

Note: word1 and word2 are both in the list.
'''

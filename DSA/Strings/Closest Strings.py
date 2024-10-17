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
# Approach
'''
We take two pointers, iterate over the list and track the index at which the words occurs.
We store the ans as the distance between the two indices and also track the minimum if we find 
in the list further.
TC: O(N)
SC: O(1)
'''
def shortest_distance(s,word1,word2):
     # Variables to track the index
     dist1,dist2=-1,-1
     ans=float('inf')

     for i in range(len(s)):
          if s[i]==word1:
               dist1=i
          
          if s[i]==word2:
               dist2=i
          
          if dist1!=-1 and dist2!=-1:
               ans=min(ans,abs(dist1-dist2))
     
     return ans

#Test cases
testcases = [(["the", "quick", "brown", "fox", "quick"], "the", "fox", 3),(["the", "quick", "brown", "fox", "quick"], "brown", "fox", 1)]

# Test Case 3: Multiple occurrences of word1 and word2
testcases.append((["geeks", "for", "geeks", "contribute", "practice"], "geeks", "practice", 2))

# Test Case 4: Both words are at the beginning and end
testcases.append((["geeks", "for", "contribute", "practice", "geeks", "work"], "geeks", "work", 1))

# Test Case 5: Words are far apart with repeated occurrences
testcases.append((["a", "b", "a", "a", "b", "a", "b", "c"], "a", "b", 1))

# Test Case 6: Words appear only once in the list
testcases.append((["apple", "banana", "orange", "kiwi", "grape", "mango"], "banana", "grape", 3))

# Test Case 7: Same word1 and word2
# testcases.append((["cat", "dog", "cat", "fish", "cat", "dog"], "cat", "cat", 2))

# Function to run test cases
def run_tests():
    passed = 0
    for i, (s, word1, word2, expected) in enumerate(testcases):
        result = shortest_distance(s, word1, word2)
        if result == expected:
            print(f"Test Case {i+1}: Passed")
            passed += 1
        else:
            print(f"Test Case {i+1}: Failed (Expected {expected}, but got {result})")
    
    print(f"\n{passed}/{len(testcases)} Test Cases Passed")

# Run the tests
run_tests()
'''
Problem 1: Extract Middle Segment       Question From CHATGPT.
9999999999999999999999999999
Write a function extract_middle_segment that takes a list lst and an integer n as input. The function should return the middle segment of the list containing n elements. If the list has fewer than n elements, return an empty list. If n is even or the list has an even number of elements, the middle segment should be centered as closely as possible.
Steps:
Check if len(lst) < n. If so, return [].
Find the middle index and calculate the starting and ending indices for slicing.
Use slicing to return the segment.
Sample Input:
python
Copy code
lst = [1, 2, 3, 4, 5, 6, 7]
n = 3

Sample Output:
python
Copy code
[3, 4, 5] 
'''
def middle_segment(lst,n):
    if len(lst) < n:
        return []
    middle=len(lst)//2
    return lst[middle-(n//2):middle+(n//2)+ (n % 2)]

# Test cases for extract_middle_segment function
test_cases = [
    {
        "input": {"lst": [10, 20, 30, 40, 50, 60, 70, 80], "n": 4},
        "expected_output": [30, 40, 50, 60]
    },
    {
        "input": {"lst": [1, 2, 3, 4, 5], "n": 5},
        "expected_output": [1, 2, 3, 4, 5]
    },
    {
        "input": {"lst": [1, 2, 3, 4], "n": 2},
        "expected_output": [2, 3]
    },
    {
        "input": {"lst": [5, 10, 15, 20, 25, 30, 35], "n": 1},
        "expected_output": [20]
    },
    
    {
        "input": {"lst": [3, 6, 9], "n": 4},
        "expected_output": []
    },
    {
        "input": {"lst": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], "n": 5},
        "expected_output": [4, 5, 6, 7, 8]
    },
    {
        "input": {"lst": [100, 200, 300, 400, 500, 600], "n": 2},
        "expected_output": [300, 400]
    },
    {
        "input": {"lst": [42], "n": 1},
        "expected_output": [42]
    },
    {
        "input": {"lst": [8, 16, 24, 32, 40, 48], "n": 3},
        "expected_output": [24, 32, 40]
    }
]


# Function to test all cases
def test_extract_middle_segment(function):
    for i, test_case in enumerate(test_cases, 1):
        result = function(**test_case["input"])
        assert result == test_case["expected_output"], f"Test case {i} failed: got {result}, expected {test_case['expected_output']}"
        print(f"Test case {i} passed.")

test_extract_middle_segment(middle_segment)

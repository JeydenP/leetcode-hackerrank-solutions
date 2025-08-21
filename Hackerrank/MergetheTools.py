# This programs a solution to the "Merge the Tools!" problem on HackerRank.

# This solution uses textwrap to split the string into substrings of length k,
# then iterates through each substring to remove duplicate characters while maintaining order.
# Finally, it prints each processed substring on a new line.
# difficulty: Medium
# Merge the Tools!
# Problem Statement: https://www.hackerrank.com/challenges/merge-the-tools/copy-from/443363774?isFullScreen=true

import textwrap

def merge_the_tools(string, k):
    substrings = textwrap.wrap(string,k)
    for substring in substrings:
        finalresult = "" 
        for char in substring:
            if char not in finalresult:
                finalresult += char
        print(finalresult)
    

# Example usage
if __name__ == '__main__':
    string, k = "AABCAAADA", 3
    merge_the_tools(string, k)
    
    # Expected Output:
    # AB
    # CA
    # AD  
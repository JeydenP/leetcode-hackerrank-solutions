# This program takes a string as input and swaps the case of each letter in the string.
# If a letter is uppercase, it is converted to lowercase, and vice versa.
# The final result is returned as a new string with the cases swapped.
# difficulty: Easy
# sWAP cASE
# Problem Statement: https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true


def swap_case(s):
    string = [letter for letter in s]
    finalString = []
    for letter in string:
        if letter.isupper():
            finalString.append(letter.lower())
        else:
            finalString.append(letter.upper())
    
    return "".join(finalString)

# Example usage:
if __name__ == '__main__':
    s = example_input = 'HackerRank.com presents "Pythonist 2".'
    result = swap_case(s)
    print("Input String:", s)
    print("Output String:", result)
# Example Output:
# Input String: HackerRank.com presents "Pythonist 2".
# Output String: hACKERrANK.COM PRESENTS "pYTHONIST 2".

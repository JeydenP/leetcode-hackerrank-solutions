# This program takes a string and modifies it by replacing a character at a given index with another character.
# It is designed to solve the "Mutations" problem on HackerRank.
# difficulty: Easy
# Mutations
# Problem Statement: https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true


def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

if __name__ == '__main__':
    # s = input()
    # i, c = input().split()
    # hardcoded example for demonstration
    s = "abracadabra"
    i, c = 5, "k"
    s_new = mutate_string(s, int(i), c)
    print(s_new)
# Example usage:
# input: "abracadabra", 5, "k"
# output: "abrackdabra"
# This code replaces the character at index 5 in the string "abracadabra" with "k", resulting in "abrackdabra".


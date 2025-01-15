# You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.
# Input
# The only input line contains a string of n characters.
# Output
# Print one integer: the length of the longest repetition.
# Constraints

# 1 \le n \le 10^6

# Example
# Input:
# ATTCGGGA

# Output:
# 3

def repetition(dna) -> int:
    max_len = 1
    current_len = 1
    for i in range(1, len(dna)):
        if dna[i] == dna[i-1]:
            current_len += 1
        else:
            current_len = 1
        if current_len > max_len:
            max_len = current_len
    return max_len

if __name__ == '__main__':
    dna = input()
    print(repetition(dna))

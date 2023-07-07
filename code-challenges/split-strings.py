# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the missing second character of the final
# pair with an underscore ('_').

def solution(s):
    split_list = []
    pair = ''
    for char in s:
        pair += char
        if len(pair) == 2:
            split_list.append(pair)
            pair = ""
    if pair:
        split_list.append(pair + '_')

    return split_list

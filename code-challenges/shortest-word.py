# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

def find_short(s):
    word_len_list = []
    for word in s.split():
        word_len_list.append(len(word))
    shortest_len = min(word_len_list)
    return shortest_len

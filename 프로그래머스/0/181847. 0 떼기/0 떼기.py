def firsttime(word):
    for index, char in enumerate(word):
        if(char != '0'):
            return index
def solution(n_str):
    value = firsttime(n_str)
    return n_str[value:]
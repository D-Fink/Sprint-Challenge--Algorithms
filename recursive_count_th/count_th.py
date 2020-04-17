'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # if length of word is less than 2, stop recursion.
    if len(word) < 2:
        return 0
    #if first element pair = th add 1, skip next pair since it would start with h and therefor cannot match th, repeat.
    elif word[0:2] == 'th':
        return count_th(word[2:]) + 1
    #if elements != th move to next pair of elements
    else:
        return count_th(word[1:])

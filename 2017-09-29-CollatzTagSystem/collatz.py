#!/usr/bin/env python3

alphabet = ['a', 'b', 'c']
prod_rules = {'a': 'bc',
              'b': 'a',
              'c': 'aaa'}
m = 2

def computation(word):
    result = []
    while word != 'a':
        pr = word[0]
        word = word[m:]
        word += prod_rules[pr]
        result.append(word)
    return result

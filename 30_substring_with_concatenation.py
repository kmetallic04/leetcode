'''
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

'''

import unittest

def substring(string, words):
  word_count = dict(zip(words, [0] * len(words)))
  output = list()
  
  for i in range(len(words)):
    start = i * len(words[0])
    end = start + len(words[0])
    word_count[words[i]] += 1
  print(word_count)
    
  for i in range(0, (len(string) - (len(words[0]) - 1) * len(words)), len(words[0])):
    print('---------------------------------------------')
    word_count_current = dict()
    for j in range(len(words)):
      start = i + j * len(words[0])
      end = start + len(words[0])
      print(string[start:end])
      if not word_count_current.get(string[start:end]):
        word_count_current[string[start:end]] = 0
      word_count_current[string[start:end]] += 1
    
    print(word_count_current)
    if word_count_current == word_count:
      output.append(i)
      
  return output
  
print(substring("wordgoodgoodgoodbestword", ["word"]))
    

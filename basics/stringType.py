'''
Created on Oct 5, 2023

@author: Rohit.Kumar012
'''

s="You are awesome"
print('print string value :: ',s)

''' Indexing to get exact character at that particular index'''
print('print element at index 0 :: ',s[0])

''' Repeatation '''
print('print same string 3 times :: ',s*3)

''' len function to get length of string '''
print('length of string :: ',len(s))

""" Slicing for split string """
print('print string after sub string from index 0 to 4 :: ',s[0:4])
print('print string after sub string from index 4 to last index :: ',s[4:])
print('print string after sub string from index 0 to 8 :: ',s[:8])

""" -1 always represent last index """
print('print string after sub string from index -3 to -1 in reverse  :: ',s[-3:-1])

""" Example of step in slicing 
By default step value is 1 """
print('print string after sub string from index 0 to 9 and skip 1 element :: ',s[0:9:2])

""" Just reverse value of string """
print('print string in reverse from index 15:: ',s[15::-1])
print('print string in reverse :: ',s[::-1])

""" strip function to remove spaces """
t="   You are creator of your destiny   "
print('print string after removing extra space from both side :: ',t.strip())
print('print string after removing extra space from left side :: ',t.lstrip())
print('print string after removing extra space from right side :: ',t.rstrip())

""" find function to get character inside string """
print("print index of given character :: ",t.find("cre", 0, len(t)))
""" If it couldn't find that character within last index provided then it returns -1 """
print("print index of given character when character not present in given range :: ",t.find("cre", 0, 8))

""" count function to get number of occurance in string """
print('print number of occurance of given character in string :: ',t.count("e"))

""" Some useful functions """
print('print string after replace word :: ',s.replace("awesome", "super"))
print('print string after replace character :: ',s.replace("a", "A"))
print('print after converting entire string to upper case :: ',s.upper())
print('print after converting entire string to lower case :: ',s.lower())
print('print after converting only first letter of word to upper case from string  :: ',s.title())





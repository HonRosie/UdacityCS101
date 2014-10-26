# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.

#loop through each letter in source
#if letter is not in splitlist, add to temp word
#if letter is in splitlist, check to see if word is null
#if word is null, go to next iteration
#if word is not null, add word to list of words
#at the end, add the last temp word to list of words

def split_string(source,splitlist):
    tempWord = ""
    words = []

    for char in source:
        if splitlist.find(char) == -1:
            tempWord = tempWord + char
        else:
            if tempWord != "":
                words.append(tempWord)
                tempWord = ""
    if tempWord != "":
        words.append(tempWord)
    return words

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
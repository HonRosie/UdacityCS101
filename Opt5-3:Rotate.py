# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def shift_n_letters(letter, n):
    aval = ord("a")
    zval = ord("z")


    shift = ord(letter) + n
    if shift > zval:
        return chr((shift - zval) + (aval-1))
    if shift < aval:
        return chr(zval + (shift - aval + 1))
    else:
        return chr(shift)


def rotate(words, n):
  rotatedWords = ""
  for letter in words:
    if letter != " ":
      rotatedWords = rotatedWords + shift_n_letters(letter, n)
    else:
      rotatedWords = rotatedWords + letter
  return rotatedWords


print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???



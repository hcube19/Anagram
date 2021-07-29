from itertools import permutations
import enchant

d = enchant.Dict("en_US") #Dictionary
anagrams=[]
string=input("Enter the word: ")  #Input

#CHeck case=senstivity
if string.isupper() :
    case="upper"
elif string[0].isupper():
    case="capital"
else:
    case="lower"

perms = [''.join(p) for p in permutations(string.lower())] #All possible words from letters of input string
print("Possible permutation from letters of",string," \n",perms)

for words in perms:
    flag = d.check(words.lower())  #Check if the words exist or meaningful
    if flag==True and words !=string:
        if case=="upper":
            anagrams.append(words.upper())
        elif case=="capital":
            anagrams.append(words.capitalize())
        elif case=="lower":
            anagrams.append(words)
print("Possible anagrams of words " ,string," are : ",anagrams) #Print list of possible anagrams

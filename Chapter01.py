
#1.1
#Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

string = "hola"

for i in range(len(string)):
    for k in range(len(string)):
        if k == len(string):
             if ord(string[i]) == ord(string[k]):
                if i != k:
                    pass
                    print(string[k], "está repetida")

        elif k != len(string):
            if ord(string[i]) == ord(string[k:k+1]):
                if i != k:
                    pass
                    print(string[k:k+1] , "está repetida")

#1.2
#Check Permutation: Given two strings,write a method to decide if one is a permutation of the
#other.

string1 = "hola"
l_str1 = []

string2 = "holahola"
l_str2 = []

for i in range(len(string1)):
    l_str1.append(string1[:i])
l_str1.append(string1)
l_str1.pop(0)

for i in range(len(string2)):
    l_str2.append(string2[:i])
l_str2.append(string2)
l_str2.pop(0)

for i in l_str1:
    if i in l_str2:
        if i * int(len(string2) / len(i)) == string2:
            print(string2, "es una permutación de" , i)


#1.3
#URLify: Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional
# characters,and that you are given the "true" length of the string.
# (Note: If implementing in Java,please use a character
# array so that you can perform this operation in place.)


def spaceFill(link):
    words = link.split()
    fianlLink = ""
    for i in words:
        fianlLink = fianlLink + i
        if i != words[-1]: 
            fianlLink = fianlLink + "%20"

    return fianlLink
print(spaceFill("Hola amigo yo estoy bien"))


#1.4

#Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­ drome.
# A palindrome is a word or phrase that is the same forwards and backwards.A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.

string = input("Ingresa una frase: ")

format_string = string.replace(" ", "")
print(format_string)

str_alReves = ""

for i in reversed(format_string):
    str_alReves = str_alReves + i

if format_string == str_alReves:
    print("Es palindroma")

else:
    print("No es palindroma")

 # One Away: There are three types of edits that can be performed on strings: insert a character,
 # remove a character, or replace a character. Given two strings,
 # write a function to check if they are one edit (or zero edits) away.

def edit(string, result):

    list_a, list_b = list(string), list(result)
  
    repetido = (set(list_a) & set(list_b))

    flag = True

    print(abs(len(list_a) - len(repetido)))
    if abs(len(list_a) - len(repetido)) > 1:
        flag = False

    print(abs(len(list_b) - len(repetido)))
    if abs(len(list_b) - len(repetido)) > 1:
        flag = False

    print(flag)

edit("hola", "ola")
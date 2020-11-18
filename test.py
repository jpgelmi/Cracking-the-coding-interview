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
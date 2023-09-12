# Write a python program to translate a message into secret code language. Use the rules below to translate normal english
# into secret code language -
#
# CODING:
# if the word contains at least three character, remove the first letter and append it at the end
#         now append three random characters at the starting and at the end
# else:
# simply reverse the string
#
# exa = harry = ACHarryhDFG,
#
# DECODING:
# if the word contains less than three characters, reverse it.
# else:
#     remove 3 random characters from the start and end. Now remove the LAST letter AND append it to the beginning
#
# Your program should ask whether you want to code or decode

import random
def genThreeChar():
    charRand = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    random_characters = ''.join(random.choice(charRand) for _ in range(3))
    return random_characters

def countChar(word):
    i = 0
    a = 0
    for i,val in enumerate(word):
        a = i
    return int(a)+1

def reverseWord(word):
    val = countChar(word)
    val -= 1
    reverseword = ""
    while val >= 0:
        reverseword = reverseword + word[val]
        # print(reverseword)
        val -= 1
    return reverseword

def decryptword(word):
    a = word[3:]
    print("Trimmed first 3 characters", a)
    a = a[:len(a)-3]
    print("Trimmed last three characters", a)
    temp = a[len(a)-1:]
    a = temp + a[:(len(a)-1)]
    print("Fianl output decrypted = ", a)
    return a



# Driver code CODING
ch = int(input("""
1- Encrypt
2- Decryption
Enter the desired option number = """))

match ch:
    case 1:
        try:
            word = input("Input a word to encrypt = ")
            chars = countChar(word)
            temp = ""
            if chars > 3:
                tmp1 = word[0]
                nword = word[1:] + tmp1
                print("First to end = ", nword)
                temp = genThreeChar() + nword + genThreeChar()
                print("final Encrypted = ", temp)
            elif 0 < chars < 4:
                temp = reverseWord(word)
                print("Encrypted", reverseWord(word))
            else:
                print("Hay at least one character is required")
        except Exception as e:
            print("Some thing went wrong")
    case 2:
        try:
            # Decoding
            word = input("Input a word to de-encrypt = ")
            # word = temp
            chars = countChar(word)

            if 0 < chars < 4:
                print("Decrypted", reverseWord(word))
            else:
                print("Final Decrypted", decryptword(word))
        except Exception as e:
            print("Some thing went wrong")
    case _:
        print("Invalid option number..")
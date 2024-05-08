#Takes string and outputs different strings

#vowels --> becomes g, this is the new language

def translate (phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation



print(translate(input("Enter a phrase: ")))
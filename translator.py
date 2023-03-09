from gettext import translation


def translator(str):
    translation = ""
    for letter in str:
        if letter in "AEIOUaeiou":
            translation = translation + "M"
        else:
            translation = translation + letter
    return translation
print(translator(input("enter your word")))                
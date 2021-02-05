import re


def camel_case(sentence):



    # takes given sentence and splits up words
    removeSpaces = re.sub(r'\s+', ' ', sentence)
    words = removeSpaces.split()
    # checks to see if new var name is valid
    if not words[0].isalpha():
        print("Warning, you cannot name a variable with the first char as a number or symbol ")
    else:
        # creates a list to hold words
        wordsCap = []
        # for each loop to run through words
        for word in words:
            # adds words to list and capitalizes first letter
            wordsCap.append(word.title())
    # joins all words into a string and removes space
    camelCase = ''.join(wordsCap)

    # now takes the first letter and turns it to lowercase
    newWord = camelCase[0].lower() + camelCase[1:]
    newVariable = ""
    for char in newWord:
        if char.isalnum():
            newVariable += char
    return newVariable


def main():
    # takes the users input to convert to camelCase
    newVariable = input("What is the name you would like to convert to camelCase? ")
    print(camel_case(newVariable))


if __name__ == '__main__':
    main()


def main():


    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        words = file_contents.split()

        numChar = numOfChar(file_contents)

        arrayChar = numOfCharList(numChar)


        def sort_on(dict):
            return dict["num"]
        
        arrayChar.sort(reverse=True, key=sort_on)


        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document")
        print()
        print()

        for ch in arrayChar:
            print(f"The \'{ch['char']}\' character was found {ch['num']}")

        print("--- End report ---")

def numOfChar(text):
    numChars = {}
    noSpace = text.lower()

    for char in noSpace:
        if char.isalpha():
            if char in numChars:
                numChars[char] += 1
            else: 
                numChars[char] = 1
    return numChars

def numOfCharList(numCHarObject):
    charList = []

    for ch in numCHarObject:
        charList.append({"char": ch, "num": numCHarObject[ch]})

    return charList


main()

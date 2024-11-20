#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #: W0516070    
#Student Name: Valentine Byrnes 

    # YOUR CODE STARTS HERE, each line must be indented (one tab)

#Get user input: phrase, redactions (& make sure their phrase/redactions are valid in their separate contexts)
def userInput():
    fullPhrase = []
    fullPhrase = input("Type a phrase (or quit to exit program): ").lower()
    if fullPhrase == "quit":
        quit()
    validPhrase = True
    for char in fullPhrase:
        if char.isnumeric():
            validPhrase = False
            break
        elif char.lower() not in "abcdefghijklmnopqrstuvwxyz, ., !, ?":
            validPhrase = False
            break
        elif "," in char:
            validPhrase = False
            break
    if validPhrase == False:
        print("\nPlease use alphabetical letters, commas, and periods (for ends of phrases) only. Try again.\n")
        return main()
    redactedInput = input("\nType a comma-separated list of letters to redact: ").lower()
    redactedLetters = redactedInput.split(",")
    validLetters = True
    for letter in redactedLetters:
        if not letter.isalpha():
            validLetters = False
            break
    if validLetters == False:
        print("\nPlease use alphabetical letters and commas only. Try again.\n")
        return main()
    return fullPhrase, redactedLetters

#Redact the requested letters from the phrase and count the number of redacted letters
def redact(fullPhrase, redactedLetters):
    redactedString = fullPhrase
    for letter in redactedLetters:
        redactedString = redactedString.replace(letter, "_")
    numOfRedact = redactedString.count("_")
    print(f"Number of letters redacted: {numOfRedact}")
    return redactedString

#Output the redacted phrase
def outputPhrase(r):
    print(f"Redacted phrase: {r}\n")

#Call all of my functions here
def main():
    fullPhrase, redactedLetters = userInput()
    r = redact(fullPhrase, redactedLetters).capitalize()
    outputPhrase(r)
    if fullPhrase == "quit":
        quit()
    else:
        main()
    # YOUR CODE ENDS HERE

main()
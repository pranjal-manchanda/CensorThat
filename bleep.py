from cs50 import get_string
from sys import argv
import sys
"""
Program imports a list of banned words and ensures that they are censored out
from any input text.
"""
# Create a set of banned words
bannedWords = set()

def main():
    # Ensure correct number of command line arguments passed in
    if not len(argv) == 2:
        print("Usage: python bleep.py dictionary")
        sys.exit(1)
    # Function to load banned words into bannedWords set
    load()
    # Get user input for a string they would like to censor
    message = get_string("What message would you like to censor?\n")
    # Remove punctuations and store message as a list of words
    message = message.split()
    # Call function to censor message
    message = censor(message)
    # Convert message list into a string separated by spaces
    print(" ".join(str(x) for x in message))

# Function to load list of banned words
def load():
    # Open file passed in as command line argument
    file = open(argv[1], "r")
    # Add words from file into banned words set after removing the \n
    for line in file:
        bannedWords.add(line.rstrip("\n"))
    file.close()
    return True

# Function to censor the words passed in as input string by user
def censor(message):
    # Iterate through each word in message list and check if the lowercase (case-insensitive)
    # version of that exists in banned words
    # If it does, replace the length of that word with that many *
    # Return message
    length = len(message)
    for i in range(length):
        if message[i].lower() in bannedWords:
            message[i] = "*" * len(message[i])
    return message

# Call main when the program starts
if __name__ == "__main__":
    main()
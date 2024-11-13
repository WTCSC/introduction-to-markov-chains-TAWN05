import random
import re
import argparse

"""
Create the sample text and the dictionary to store word transitions

TODO: Replace the sample text with a larger text for more interesting results
"""
#Opens a file and reads the contents
file = open("pg84.txt", "r")
text = file.read()

#Creates the main dictionary for the chain
transitions = {}

"""
Build the Markov Chain

1. Split the text into words
2. Iterate over the words
3. For each word, add the next word to the list of transitions

TODO: Handle punctuation and capitalization for better results
"""

#Defines the the punctuation the program will recognise
delimiters = [",", ";", ":", "?", "!", "."]

#Defines the words used
words = text.split()

for i in range(len(words) - 1):

    #Defines the current word to be writin to the dictionary and then next to be added to the list of words for the current word
    current_word = words[i]
    next_word = words[i + 1]

    #Used to make sure the program will add the same word twice if it hase punctuation
    b = True

    #For each charter in current word
    for x in current_word:

            #For each punctuation mark in delimiters
            for y in delimiters:

                #Strips the next word of any punctuation
                next_word = "".join(next_word.split(y))

                #Checkes if the charater in current word is a punctuation make
                if x == y:

                    #If a word is determend to have punctuation dont add it again after alread adding it here
                    b = False

                    #Stripes all punctuation off the current word
                    current_word = "".join(current_word.split(y))

                    #If the current word is not a entry in the dictionary than add it to the dictionary
                    if current_word not in transitions:
                        transitions[current_word] = []

                    #Add the punctuation mark to the list of words the current word can be chosen from
                    transitions[current_word].append(x)

                    #Debug this creates a super interesting bug (I WONDER IF YOU CAN FIND IT OUT??!!)
                    #next_next_word = "".join(next_next_word.split(y))

                    #If the punctuation mark is not in the dictionary than add it
                    if x not in transitions:
                        transitions[x] = []

                    #Adds the next word to the list of word the punctuation mark can pick from
                    transitions[x].append(next_word)

    #If the word has not already been added by the above than add it.
    if b == True:
        if current_word not in transitions:
            transitions[current_word] = []
        transitions[current_word].append(next_word)



"""
Generate new text using the Markov Chain, starting with a given word and
generating a specified number of words:

1. Start with the given word
2. Add the word to the result list
3. For the specified number of words:
    a. If the current word is in the transitions dictionary, choose a random next word
    b. Add the next word to the result list
    c. Update the current word to the next word
4. Return the generated text as a string

TODO: Clean up the generated text for better formatting and readability,
e.g., capitalization, punctuation, line breaks, etc.
"""

def generate_text(start_word, num_words):

    #Starts the chain and adds the starting word to the system
    current_word = start_word

    #Defines the list of words used for the creation of the final string
    result = []

    #Loop as many times in num_words example num_words=100 loops 100 times 
    for _ in range(num_words - 1):

        #Used to add the word to results list if it is fount the next word does not have a punctuation mark
        z = False

        #Checks to see if the current word is assosiated with a list of words in the dictionary
        if current_word in transitions:

            #If the word is valid it picks from the list of words assosiated with that word in the dictionary
            next_word = random.choice(transitions[current_word])

            # Loop for each punctuation mark in delimiters
            for y in delimiters:

                # If the NEXT word is equal to a punctuation mark
                if next_word == y:

                    # Makes sure the same word is not added below
                    z = True

                    # Takes the current word and combines it with the punctuation mark of the next word making the punctuated current word
                    current_punctuated_word = current_word + "" + next_word

                    # Adds the punctuated word the the result list
                    result.append(current_punctuated_word)

                    # Sets a new random word after the current word has been added. The original random word picker could not be used because I am adding the current word to results not the next word
                    current_word = random.choice(transitions[next_word])

                    # Debug
                    #print(f"setting current word to '{current_word}' ")

            # If the current word was not added above it is added here
            if z == False:
                result.append(current_word)

                #sets current word to next word. This works because this is not adding the next word to the end of the current word
                current_word = next_word
        
        # If the current word is not in translations than break
        else:

            # Debug
            #print(f"this word is not in translations {current_word}")
            break
    # Joins all words together by a space and returns the output
    return " ".join(result)

"""
Example usage, generating 10 words starting with "Mary"

TODO: Accept user input for the starting word and number of words to generate
"""

#Debug
#print(generate_text(("today"), 500))


def main():

    # Describes the function of the function
    parser = argparse.ArgumentParser(description='Generates a chain of words based on starting word and number of words for the chain')

    # Defines the "start_word" based on user imput
    parser.add_argument('start_word', help='Defines the word for the chain to start off from')
    
    # Defines the "num_words" based on user imput
    parser.add_argument('num_words', type=int, help='Defines the number of words long the chain should be')

    # She parsing on my args
    args = parser.parse_args()

    # Makes a variable to display answer in the correct format.
    chain = generate_text(args.start_word, args.num_words)
    print(chain)

# May you embark on the annals of QUD Joppa will be needing you (if you want to understand this obscure referance to a game nobody plays look up caves of qud markcov chains)
if __name__ == '__main__':
    main()

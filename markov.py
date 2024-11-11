import random
import re

"""
Create the sample text and the dictionary to store word transitions

TODO: Replace the sample text with a larger text for more interesting results
"""
text = "Mary, had: a little lamb its fleece was white as snow"
transitions = {}

"""
Build the Markov Chain

1. Split the text into words
2. Iterate over the words
3. For each word, add the next word to the list of transitions

TODO: Handle punctuation and capitalization for better results
"""
punctuated_text = []
delimiters = [",", ":", ";", ":"]
words = text.split()
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    for x in current_word:
        if x == "," or x == ";" or x == ":" or x == ".":
            current_word.append(punctuated_text)
            for x in delimiters:
                current_word = "".join(current_word.split(delimiters))
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
    current_word = start_word
    result = [current_word]
    for _ in range(num_words - 1):
        if current_word in transitions:
            next_word = random.choice(transitions[current_word])
            result.append(next_word)
            current_word = next_word
        else:
            break
    return " ".join(result)

"""
Example usage, generating 10 words starting with "Mary"

TODO: Accept user input for the starting word and number of words to generate
"""
print(transitions)
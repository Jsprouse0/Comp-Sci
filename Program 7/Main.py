'''
Author: Jacob Sprouse
Assignment title: Program 7
Assignment Description: Word frequency
Due Date: 05/12/2023
Date Created: 05/01/2023
Date Last Modified: 05/09/2023

'''
import string

freq_words    = dict()
sorted_words  = set()
all_words     = list()

# Input asks and opens file
file_name = input("Please enter a file name: ")
file      = open(file_name)

# Process loops through lines in file and stores char in list/set
for line in file:
    for word in line.split():
        for character in ['.', ',']:
            word = word.replace(character, '')
        all_words.append(word)
        sorted_words.add(word)

for word1 in sorted_words:
    for word2 in all_words:
        if word1.lower() == word2.lower():
            if word1 in freq_words:
                freq_words[word1] += 1
            else:
                freq_words[word1] = 1

sorted_dict = sorted(freq_words)

file.close()

# Output prints extra lines for spacing and prints the dict
print('\n\n')

for i in sorted_dict:
    print(f'{i}{freq_words[i]}')










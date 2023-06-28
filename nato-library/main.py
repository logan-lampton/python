# NOTE on format: new_list = [new_item for item in list if test]
# new_dictionary = {new_key:new_value for (key, value) in dictionary.items() if text}
# ITERATE PANDA ROWS: for (index, row) in data_frame.iterrows(): print(row.the_value)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    # print(value)
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)


#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

print("Let's turn any word into the NATO phonetic alphabet!")
user_word = input("Provide a word: ").upper()

# for letter in user_word:
#     print(phonetic_dictionary[letter])

output = [phonetic_dictionary[letter] for letter in user_word]
print(output)

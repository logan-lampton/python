# TODO: Create a letter using starting_letter.txt

PLACEHOLDER = "[name]"

# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter_contents = starting_letter.read()
    for name in names:
        formatted_name = name.strip("\n")
        formatted_letter = letter_contents.replace(PLACEHOLDER, formatted_name)
        with open(f"./Output/ReadyToSend/letter_for_{formatted_name}.txt", mode="w") as prepared_letter:
            prepared_letter.write(formatted_letter)




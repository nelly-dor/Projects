TAG = "[name]"

with open("Input/Names/invited_names.txt", mode="r") as names:
    invited_names = names.readlines()

with open("Input/Letters/starting_letter.txt",mode="r") as template:
    letter_template = template.read()
    for name in invited_names:
        stripped_name = name.strip()
        new_letter = letter_template.replace(TAG, stripped_name)
        with open(f"Output/ReadyToSend/Letter_for_{stripped_name}",mode="w") as final_letter:
            final_letter.write(new_letter)




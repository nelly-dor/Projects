import pandas

WELCOME_LABEL = "Welcome to the NATO Phonetic code generator ! Type 'exit' to leave."
EXIT_LABEL = "Goodbye"

#Create dictionary from CSV data
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index,row) in nato_data.iterrows()}


#Create a list of the phonetic code words from a word that the user inputs.
print(WELCOME_LABEL)
loop_on = True
while loop_on:
    user_word = input("Type a word : \n")
    if user_word.lower() == "exit":
        print(EXIT_LABEL)
        break
    codeList = [nato_dict[letter.upper()] for letter in user_word]
    print(codeList)

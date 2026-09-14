import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (_, row) in nato_df.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def retry():
    user_input = input("Enter a word: ")
    try:
        user_nato_list = [nato_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the Alphabet please.")
        retry()
    else:
        print(user_nato_list)

retry()

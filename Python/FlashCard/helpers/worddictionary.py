import pandas
import random

class WordDictionary:

    def __init__(self):
        try:
            df = pandas.read_csv("data/words_to_learn.csv")
        except FileNotFoundError:
            print("No file called 'words_to_learn.csv' found, switching to default 'french_words.csv'...")
            df = pandas.read_csv("data/french_words.csv")

        self.df_dict= df.to_dict(orient="records")
        self.dict_size = len(self.df_dict)
        self.word_index = 0

    def set_random_index(self):
        self.word_index = random.randint(0, self.dict_size + 1)

    def get_word(self, lang):
        return self.df_dict[self.word_index][lang]

    def get_data_dict(self):
        dict_copy = self.df_dict.copy()
        return dict_copy












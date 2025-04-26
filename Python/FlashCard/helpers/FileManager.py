import pandas
import os

class FileManager:
    def __init__(self, data_dict):
        self.dd = data_dict

    def saveFile(self):
        df = pandas.DataFrame(self.dd)
        try:
            os.remove("data/words_to_learn.csv")
        except FileNotFoundError:
            print("No file 'words_to_learn.csv', creating one...")
        df.to_csv("data/words_to_learn.csv", index=False)

    def removeItem(self, word,lang):
        for v in self.dd:
            if v[lang] == word:
                self.dd.remove(v)
import re

class ProcesarTexto:
    def __init__(self,text):
        self.text=text
        self.text_list=(re.findall(r'[A-Za-z]+',self.text))
    def number_of_words(self):
        n_words=len(self.text_list)
        return n_words

    def number_of_characters(self):
        n_characters=self.text.strip()
        return len(n_characters)

    def frequency_words(self):
        words_frequency=[(self.text_list.count(word),word) for word in set(self.text_list)]
        return sorted(words_frequency,reverse=True)
    def lexical_density(self):
        return (len(set(self.text_list))/len(self.text_list))*100
        
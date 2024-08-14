class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = [*file_names]

    def get_all_words(self):
        all_words = {}
        symbols_check = [',', '.', '=', '!', '?', ';', ':', ' - ']
        name = self.file_names
        for current_name in name:
            with open(current_name, encoding='utf-8') as file:
                string = file.read()
                string = string.lower()
                for symb in symbols_check:
                    string = string.replace(symb,'')
                string = string.split()
                all_words[current_name] = string
        return all_words

    def find(self,word):
        find_dict = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word in words:
                position = words.index(word)
                find_dict[name] = position+1
        return find_dict

    def count(self,word):
        count_dict = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            words_count = words.count(word)
            count_dict[name] = words_count
        return count_dict

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
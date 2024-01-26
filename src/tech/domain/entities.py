class TechCaseEntity:

    def find_longest_word(self, input):

        if not isinstance(input, str):
            raise TypeError("O input deve ser uma string.")

        words = [input[i:i+n]
                 for i in range(len(input)) for n in range(2, len(input) - i + 1)]

        longest_word = max(words, key=len, default="")

        singular_words = list(set(words))
        singular_words.sort(key=len, reverse=True)

        return longest_word, singular_words

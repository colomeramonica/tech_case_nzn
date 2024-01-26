class TechCaseEntity:

    def find_longest_word(input):

        if not isinstance(input, str):
            raise TypeError("O input deve ser uma string.")

        if not input.isalpha():
            raise TypeError("O input só deve conter letras.")

        words = [input[i:i+n]
                 for i in range(len(input)) for n in range(2, len(input) - i + 1)]

        biggest_word = max(words, key=len, default="")

        singular_words = list(set(words))
        singular_words.sort(key=len, reverse=True)

        return biggest_word, singular_words

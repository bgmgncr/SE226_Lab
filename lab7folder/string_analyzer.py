from string_package import reverse_string, capitalize_words, remove_punctuation, count_characters, count_words, average_word_length

def main():
    sentence = input("Enter a sentence: ")

    reversed_str = reverse_string(sentence)
    capitalized_str = capitalize_words(sentence)
    clean_sentence = remove_punctuation(sentence)

    print("reverse_string:", reversed_str)
    print("capitalize_words:", capitalized_str)
    print("remove_punctuation:", remove_punctuation(sentence))
    print("Character Count:", count_characters(clean_sentence))
    print("Word Count:", count_words(clean_sentence))
    print("Average Word Length:", average_word_length(clean_sentence))

if __name__ == "__main__":
    main()

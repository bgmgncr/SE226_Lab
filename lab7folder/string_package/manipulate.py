def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def remove_punctuation(s):
    import string
    return ''.join(char for char in s if char not in string.punctuation)

if __name__ == "__main__":
    print(reverse_string("eyedipadanadapideye"))
    print(reverse_string("Ey edip Adana'da pide ye."))
    print(remove_punctuation("Ey edip Adana'da pide ye."))
    print(capitalize_words("Ey edip Adana'da pide ye."))

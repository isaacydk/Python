def main():
    sentence = input("Input: ")
    print(shorten(sentence))

def shorten(word):
    for vowel in "aeiouAEIOU":
        word = word.replace(vowel, "")

    return word

if __name__ == "__main__":
    main()
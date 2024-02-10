print("hello world")


def word_count(string):
    return string.split()


def letter_count(string):
    letters = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }

    lowered_string = string.lower()

    words = word_count(lowered_string)
    for word in words:
        for letter in word:
            if letter in letters:
                letters[letter] += 1
            else:
                pass

    return letters


def report(words, letters):
    def sort_on(dict):
        return dict["num"]
    print(f"Words found: {words}")

    letter_list = []

    for letter in letters:
        letter_list.append({"letter": letter, "num": letters[letter]})

    letter_list.sort(reverse=True, key=sort_on)

    for letter in letter_list:
        print(f"the letter \"{letter["letter"]}\" was found {letter["num"]} times!")

    print("========== End of Report ==========")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        number_of_words = len(word_count(file_contents))
        number_of_letters = letter_count(file_contents)

        report(number_of_words, number_of_letters)


main()

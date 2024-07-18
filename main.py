
def main():
    book_path = "/books/frankenstein.txt"
    book = open_file(book_path)

    print(f"{num_words(book)} Found!")
    print(count_letters(book))


def open_file(path):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents
    
def num_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = "".join(text.lower().split())
    letter_set = {
        "a":0,
        "b":0,
        "c":0,
        "d":0,
        "e":0,
        "f":0,
        "g":0,
        "h":0,
        "i":0,
        "j":0,
        "k":0,
        "l":0,
        "m":0,
        "n":0,
        "o":0,
        "p":0,
        "q":0,
        "r":0,
        "s":0,
        "t":0,
        "u":0,
        "v":0,
        "w":0,
        "x":0,
        "y":0,
        "z":0,
    }
    for letter in letters:
        if letter in letter_set:
            letter_set[letter] += 1
    letter_arr = []

    for letter in letter_set:
        tmp = {"char":letter, "num":letter_set[letter]}
        letter_arr.append(tmp)
    
    letter_arr.sort(reverse=True, key=sort_on)
    return letter_arr

def sort_on(dict):
    return dict["num"]
main()

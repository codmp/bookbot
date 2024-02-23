def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Number of words in document: {num_words}")
    for letter in get_letter_count(text):
        print(f"{letter['letter']}: {letter['count']}")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letter_count(text):
    letter_dict = {}
    letters = []
    for letter in text:
        lowered = letter.lower()
        if letter_dict.__contains__(lowered):
            letter_dict[lowered] += 1
        else:
           letter_dict[lowered] = 1
    for key in letter_dict:
        if key.isalpha():
            letters.append({"letter": key, "count": letter_dict[key]})
    letters.sort(reverse=True ,key=lambda dict : dict["count"])
    return letters


main()
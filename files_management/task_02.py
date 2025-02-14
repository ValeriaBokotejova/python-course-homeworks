def count_words_in_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print("File not found.")
        return 0

filename = "sample.txt"

word_count = count_words_in_file(filename)
print(f"The file contains {word_count} words.")

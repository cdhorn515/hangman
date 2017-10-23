
def main():
    path = "/usr/share/dict/words"
    word_length_3_to_8 = []
    with open(path) as file:
        words = file.split()
    for word in words:
        if len(word) >= 3 and len(word) <= 8:
        word_len_3_to_8.append(word)    


if __name__ == "__main__":
    main()

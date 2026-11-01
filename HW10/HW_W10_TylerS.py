def main():
    #list for word count
    word_count = []

    try:
        file = open("text.txt", "r")

        for line in file:
            words = line.split()
            word_count.append(len(words))

        file.close()

    #handles error
    except IOError:
        print("Could not open text.txt")
        return

    #check if the file is empty
    if len(word_count) == 0:
        print("The file is empty")
        return

    #calculates the average words per line
    total_words = sum(word_count)
    average = total_words / len(word_count)

    #prints average
    print(f"Average number of words per line: {average}")

if __name__ == "__main__":
    main()

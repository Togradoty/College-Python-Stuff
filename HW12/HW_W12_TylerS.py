import pickle

def main():
    #creates the dictionary
    word_counts = {}

    #opens file
    file = open("text.txt", "r")

    for line in file:
        words = line.split()

        #counts the words
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    file.close()
    
    #displays the words alphabetically and their counts
    print(f"{'word':<25}occurrences")
    print("-" * 40)

    for word in sorted(word_counts):
        print(f"{word:<25}{word_counts[word]}")

    #saves dictionary to a binary file
    output_file = open("word_frequency.dat", "wb")
    pickle.dump(word_counts, output_file)
    output_file.close()

if __name__ == "__main__":
    main()
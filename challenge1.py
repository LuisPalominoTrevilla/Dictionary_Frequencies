def read_from_file(file):
    """
    :param file: The file words are going to be read from
    :return: a list with the words inside the file
    """
    lista = []
    try:
        f = open(file, 'r')
        for line in f:
            line = line.strip('\n')  # Get rid of the \n at the end of each line
            lista += line.split(" ")  # get every word of the line and store it inside a list
        f.close()
    except IOError:
        print("Cannot open " + file)
    return lista


def count_frequency(words):
    """
    :param words: List of words
    :return: A dictionary with frequencies of words
    """
    frequency_words = {}
    for word in words:  # iterate over the list
        if word not in frequency_words.keys():  # If the word is not already inside the dictionary's keys, create it
            frequency_words[word] = 1
        else:
            frequency_words[word] += 1
    return frequency_words


def print_word_frequencies(word_frequencies):
    """
    This function fancy prints a dictionary with word frequencies
    :param word_frequencies: Dictionary with frequencies of words
    :return: None
    """
    for word in word_frequencies.keys():
        print(word + ": " + str(word_frequencies[word]))


words = read_from_file("words.txt")  # Create a list of words
words_frequency = count_frequency(words)  # Create a word frequencies based on the words
print(words_frequency)

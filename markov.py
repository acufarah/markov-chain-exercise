"""Generate Markov text from text files."""

from random import choice

from sys import argv


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    return open(file_path).read()


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}
    words = text_string.split()

    i = 0
    while i < len(words)-2:
        key = (words[i], words[i+1])
        chains[key] = chains.get(key, []) + [words[i + 2]]
        i += 1

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    # keys = (list(chains.keys()))
    # key_capital = []
    # for key in keys:
    #     if key[0][0].isupper():
    #         key_capital.append(key)
    # key_start = choice(key_capital)
    key_capital = []
    keys = (list(chains.keys()))
    for key in keys:
        if key[0][0].isupper():
            key_capital.append(key)
    key_start = choice(key_capital)

    words.extend([key_start[0], key_start[1]])

    key = key_start

    while key in chains:
        value_list = chains.get(key)
        rand_value = choice(value_list)
        words.extend([rand_value])
        key = (key[1], rand_value)
        if len(words) > 40 and key[1][-1] in "?.!":
            break


    return " ".join(words)


# def capitalize_chain(chains):
#     key_capital = []
#     keys = (list(chains.keys()))
#     for key in keys:
#         if key[0][0].isupper():
#             key_capital.append(key)
#     key_start = choice(key_capital)
#     return key_start[0] + " " + key_start[1] + " " + make_text(chains)


input_path = 'spirits.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)



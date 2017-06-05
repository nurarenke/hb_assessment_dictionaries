"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    counting_by_distinct_words = {}

    # splits the string into seperate words
    words = phrase.split()

    # iterate through each word, assign it as a key to the dict
    # then see if you have the key and add one every time you can count the key
    for word in words:
        counting_by_distinct_words[word] = counting_by_distinct_words.get(word, 0) + 1

    return counting_by_distinct_words


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    # I created a dictionary with the list of melon names and prices
    price_by_melon_name = {
    "Watermelon" : 2.95,
    "Cantaloupe" : 2.50,
    "Musk" : 3.25,
    "Christmas" : 14.25,
    }

    # when the melon name is called it will get the corresponding price value
    return price_by_melon_name.get(melon_name, "No price found")


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """
    # created an empty dictionary
    word_length_dict = {}

    # loop through the list of words and save the key as the length
    for word in words: 
        key = len(word)

        # see if the key exists in the dictionary
        # If not, then I add the length key with the word as the value
        if key not in word_length_dict:
            word_length_dict[key] = [word]

        # If the key is already in the dictionary, then append the word to the list of words
        # Then sort the list of words
        else:
            word_length_dict[key].append(word)
            word_length_dict[key] = sorted(word_length_dict[key])     
        
    # return the dictionary items as tuples and sort them
    return sorted(word_length_dict.items())

def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    # Create a dictionary of the table
    # Also, side note: 
    # I learned that if you hold down the alt key you can add text to muliple lines in sublime
    pirate_to_english_dict = {
    "sir"         : "matey",
    "hotel"       : "fleabag inn",
    "student"     : "swabbie",
    "man"         : "matey",
    "professor"   : "foul blaggart",
    "restaurant"  : "galley",
    "your"        : "yer",
    "excuse"      : "arr",
    "students"    : "swabbies",
    "are"         : "be",
    "restroom"    : "head",
    "my"          : "me",
    "is"          : "be"
    }
    # Created an empty list to store my sentence
    translated_sentence = []

    # Split the phrase into a list of words
    phrase_list = phrase.split(' ')

    # Iterated through the list of words
    for word in phrase_list:

        # If the word in the phrase matches our key in our dictionary
        # Get the value from that matching key
        # Append the value to our translated sentence list
        if word in pirate_to_english_dict.keys():
            translation = pirate_to_english_dict.get(word, word)
            translated_sentence.append(translation)

        # If the word does not match any of keys in our dictionary
        # Then just append the word to our translated sentence list
        else:
            translated_sentence.append(word)

    # Return tranlsated sentence list and turn it into a string
    return " ".join(translated_sentence)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    # create an empty list for results and add the first word from names
    results = []
    results.append(names[0])

    # delete the first word from names, so that you can't use that word again
    del names[0]

    words_by_first_letter_dict = {}

    # Store the first letter of each word in the list as the key to the dict
    for name in names:
        key = name[0]

        # If the key is not already in the dict, create the key with name
        if key not in words_by_first_letter_dict:
            words_by_first_letter_dict[key] = [name]

        # Else the key is already in the dict, so append the name to the list of values 
        else:
            words_by_first_letter_dict[key].append(name)

    # Then I want to find the last letter of the first word to use to search in our dictionary
    first_word = results[0]
    last_letter = first_word[-1]

    # While the last letter is a key in the dictionary continue below
    while last_letter in words_by_first_letter_dict.keys():

        # Add the first word in our list of values to the results list
        word_to_append = words_by_first_letter_dict[last_letter][0]
        results.append(word_to_append)

        # Then we can delete that word we used from our list of values
        del words_by_first_letter_dict[last_letter][0]

        # If all that is left is an empty list, delete the key from the dictionary
        if words_by_first_letter_dict[last_letter] == []:
            words_by_first_letter_dict.pop(last_letter)

        # Then we reassign the last letter to the last letter of the word we just appended.
        last_letter = word_to_append[-1]

    return results

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print

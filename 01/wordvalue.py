from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    
    with open(DICTIONARY, "r") as dict:
        return dict.read().split()

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    
    score = 0
    for letter in word.upper():
        if letter in LETTER_SCORES:
            score += LETTER_SCORES[letter]
    return score

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    
    max_score = 0
    max_score_word = ""
    for word in words:
        score = calc_word_value(word)
        if score > max_score:
            max_score = score    
            max_score_word = word
        score = 0

    return max_score_word

if __name__ == "__main__":
    print(max_word_value())
    #pass # run unittests to validate


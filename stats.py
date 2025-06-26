def get_word_count(text):
    """Returns total number of words in the text."""
    return len(text.split())

def get_char_frequency(text):
    """Returns frequency of each relevant character in the text."""
    frequency = {}
    for char in text.lower():
        if char.isalpha() or char in ['æ', 'â', 'ê', 'ë', 'ô']:
            frequency[char] = frequency.get(char, 0) + 1
    return frequency

def sort_char_frequency(frequency_dict):
    """Returns a new dict sorted by frequency descending."""
    sorted_items = sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_items)

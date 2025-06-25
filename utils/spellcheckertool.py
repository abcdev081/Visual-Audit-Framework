# utils/spellcheckertool.py

from spellchecker import SpellChecker


def check_spelling(text):
    spell = SpellChecker()
    words = text.split()
    misspelled = spell.unknown(words)
    errors = {}
    for word in misspelled:
        errors[word] = spell.correction(word)
    return errors

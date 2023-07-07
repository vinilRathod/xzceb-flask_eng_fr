"""
    This file is used for translation.
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
        This function translates english text to french.
    """
    french_text = MyMemoryTranslator(source = "english india",
    target = "french").translate(english_text)
    return french_text

def french_to_english(french_text):
    """
        This function translates french text to english.
    """
    english_text = MyMemoryTranslator(source = "french",
    target = "english india").translate(french_text)
    return english_text

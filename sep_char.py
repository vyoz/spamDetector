import sys
import re

def remove_special_chars(string):
    # pattern to match special characters
    pattern = r'[^\u4e00-\u9fff\w\s]'
    clean_string = re.sub(pattern, ' ', string)
    # add space at the beginning and end of each English word
    clean_string = re.sub(r'(\b\w+\b)', r' \1 ', clean_string)
    # add space between Chinese words
    clean_string = re.sub(r'([\u4e00-\u9fff])', r' \1 ', clean_string)
    # remove multiple spaces with a single space
    clean_string = re.sub(r'\s+', ' ', clean_string)
    return clean_string

def separate_chinese_and_english(text):
    return remove_special_chars(text)

def separate_chinese_and_english_orig(text):
    # Define regular expressions for Chinese and English
    chinese_pattern = re.compile(r'([\u4e00-\u9fff])')  # Unicode range for Chinese characters
    english_pattern = re.compile(r'([a-zA-Z0-9\.\/\*\\]+)')         # English alphabet

    # Separate Chinese characters with space
    text = chinese_pattern.sub(r'\1 ', text)
    # Separate English words with space
    text = english_pattern.sub(r' \1 ', text)
    
    return text.strip()


import sys
import re

def separate_chinese_and_english(text):
    # Define regular expressions for Chinese and English
    chinese_pattern = re.compile(r'([\u4e00-\u9fff])')  # Unicode range for Chinese characters
    english_pattern = re.compile(r'([a-zA-Z0-9\.\/\*\\]+)')         # English alphabet

    # Separate Chinese characters with space
    text = chinese_pattern.sub(r'\1 ', text)
    # Separate English words with space
    text = english_pattern.sub(r' \1 ', text)
    
    return text.strip()


#Write a program using filter() to select all words from a list that start with ovwel.
def starts_with_vowel(word):
    return word[0].lower() in 'aeiou'
words = ["apple", "banana", "orange", "grape", "umbrella", "ink", "sky"]
vowel_words = list(filter(starts_with_vowel, words))
print(vowel_words)
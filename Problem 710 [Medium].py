"""
This problem was asked by Dropbox.

Given a string s and a list of words words, where each word is the same length, find all starting indices of
substrings in s that is a concatenation of every word in words exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return [0, 13], since "dogcat" starts at
index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there are no substrings composed of "dog"
and "cat" in s.

The order of the indices does not matter.
"""


def find_substring_indexes(s: str, words: list) -> list:
    result = []
    word_length = len(words[0])
    append_word_length = len(words) * word_length
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for i in range(len(s) - append_word_length + 1):
        temp_word_count = word_count.copy()
        for j in range(i, i + append_word_length, word_length):
            word = s[j:j + word_length]
            if word not in temp_word_count or temp_word_count[word] == 0:
                break
            temp_word_count[word] -= 1
        else:
            result.append(i)
    return result


print(find_substring_indexes(s="dogcatcatcodecatdog", words=["cat", "dog"]))
print(find_substring_indexes(s="barfoobazbitbyte", words=["dog", "cat"]))

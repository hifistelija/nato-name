import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {
    row.letter: row.code for _, row in df.iterrows()
}

print([nato_alphabet.get(char, char) for char in "ILKKA"])
# iterates each letter in the word "ILKKA"
# .get takes in to arguments: 1.key to lookup in the dictionary, 2.value to return if key is not found
# for example if letter "L" is not dictionary key return value from get is "L"
# if the key is found get return value that key holds
# iterrows produces tuple in format of (index, row)
# row.letter accesses the value in the 'letter' column and row.code for value in the 'code' column
# row is a Pandas Series and using the dot notation is equivalent to using the bracket notation row['letter']'

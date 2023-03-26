import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {
    row.letter: row.code for _, row in df.iterrows()
}


def name_to_nato(name):
    name_upper = name.upper()
    nato_spelling = [nato_alphabet.get(char, char) for char in name_upper]
    return ", ".join(nato_spelling)


name = input("Enter you name: ")
nato_name = name_to_nato(name)
print(f"Your name in the NATO phonetic alphabet: {nato_name}")

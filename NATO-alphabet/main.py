import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phone_dict = {row['letter']:row['code'] for (index, row) in data.iterrows()}
print(phone_dict)


def gen_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output = [phone_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the aplhabets please ")
        gen_phonetic()
    else:
        print(output)

gen_phonetic()
import codecs


def remove_punctuation(string_to_analyze):
    set_with_non_letters = {"-", ",", ".", "?", "!", ":", ";", "[", "]", "(", ")", "*", "!", "@", '"', "'", '\n', '\r',
                            " ", '…', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '»', '«', '>', '¿', '·', '$'}
    string_non_letters_only = ""
    for character in string_to_analyze:
        if character not in set_with_non_letters:
            string_non_letters_only = string_non_letters_only + character
    string_non_letters_only = string_non_letters_only.lower()  # all lower to count
    return string_non_letters_only


def count_letters(string_to_analyze):
    dictionary_letter_amount = {}
    string_non_letters_only = remove_punctuation(string_to_analyze)
    for character in string_non_letters_only:
        if character == 'ď':
            dictionary_letter_amount['ď'] = dictionary_letter_amount['d'] + 1
        elif character in dictionary_letter_amount:
            dictionary_letter_amount[character] = dictionary_letter_amount[character] + 1
        else:
            dictionary_letter_amount[character] = 1
    sort_on_values(dictionary_letter_amount)
    return dictionary_letter_amount


def sort_on_values(dictionary):
    sorted_values = sorted(dictionary.values(), reverse=True)
    sorted_dictionary = {}
    for value in sorted_values:
        for key in dictionary.keys():
            if dictionary[key] == value:
                sorted_dictionary[key] = dictionary[key]
                break
    print(sorted_dictionary)
    return sorted_dictionary


chosen_language = input("""Enter a language code
     EN for english
     DE for german
     ES for spanish
     VI for vietnamese
     LT for lithuanian
     EL for greek""")

chosen_language = chosen_language.upper()
chosen_language = chosen_language + ".txt"

if (chosen_language == "EN.txt"
        or chosen_language == "DE.txt"
        or chosen_language == "VI.txt"
        or chosen_language == "ES.txt"
        or chosen_language == "LT.txt"
        or chosen_language == "EL.txt"):
    file = codecs.open(chosen_language, "r", 'utf8')
else:
    print("""Choose a correct language code:
    EN for english
    DE for german
    ES for spanish
    VI for vietnamese
    LT for lithuanian
    EL for greek""")

string_letters_only = ""

for line in file:
    if len(line) > 5:  # excluding rome numbering I,II t/m XXVII
        line.strip().split(':')
        string_letters_only = string_letters_only + line

dictionary_letter_amount = count_letters(string_letters_only)

alphabet = []
for character in dictionary_letter_amount.keys():
    if character == 'ď':
        alphabet = alphabet + ['ď']
    else:
        alphabet = alphabet + [character]
    alphabet.sort()
print('alphabet: ', alphabet)

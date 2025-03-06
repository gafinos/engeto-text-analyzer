"""
projekt_1: první projekt do Engeto Online Python Akademie

author: Václav Špaček
email: gafinos@gmail.com
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

SPLIT = "-" * 40

users = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}


login = input('Username: ')
password = input('Password: ')
if users.get(login) == password:
    print(f"Welcome to the app, {login}!\nWe have {len(TEXTS)} texts to be analysed.")
else:
    print("Unregistered user or invalid password. Terminating the program.")
    exit()

print(SPLIT)

chosen_text = input(f"Enter the number between 1 and  {len(TEXTS)} to select: ")

if not chosen_text.isdigit():
    print("Not a number. Terminating the program")
    exit()
elif 0 > int(chosen_text) > len(TEXTS):
    print("Wrong text number. Terminating the program")
    exit()

print(SPLIT)

source_text = TEXTS[int(chosen_text) - 1]

word_count = len(source_text.split())

titlecase_count = 0
uppercase_count = 0
lowercase_count = 0
numeric_count = 0
numeric_sum = 0


word_sizes = {}

for word in source_text.split():

    if len(word) in word_sizes.keys():
        word_sizes[len(word)] += 1
    else:
        word_sizes[len(word)] = 1
    
    if word.istitle():
        titlecase_count += 1
    if word.isupper():
        uppercase_count += 1
    if word.islower():
        lowercase_count += 1
    if word.isnumeric():
        numeric_count += 1
        numeric_sum += int(word)

print(f"There are {word_count} word in the selected text.",
      f"There are {titlecase_count} titlecase words.",
      f"There are {uppercase_count} uppercase words.",
      f"There are {lowercase_count} lowercase words.",
      f"There are {numeric_count} numeric strings.",
      f"The sum of all the numbers {numeric_sum}",
      sep='\n')

print(SPLIT)
print(f"{'LEN':>3}", f"{'OCCURENCES':<20}", 'NR.', sep='|')
print(SPLIT)

sizes_sorted = sorted(word_sizes.keys())

for size in sizes_sorted:
    bar = '*' * word_sizes[size]
    print(f"{size:>3}", f"{bar:<20}", word_sizes[size], sep='|')
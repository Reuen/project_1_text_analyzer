"""
text_analyzer.py: První projekt do Engeto Online Python Akademie

author: Patrik Zezulka
email: pat.zezulka@gmail.com
discord: Patrik Z.#8128
"""

# Pocatecni promenne:
TEXTS = ["""
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. 
""",
"""
At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.
""",
"""
The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.
"""]
separator = "-" * 40
registred_users = {"bob": "123", "ann": "pass123",
                   "mike": "password123", "liz": "pass123"}

# Prihlaseni uzivatele:
user = input("Username: ")
password = input("Password: ")

# Overeni a privitani uzivatele:
if user not in registred_users or registred_users[user] != password:
    print(separator,
          "Invalid username or password!",
          "Terminating the program...",
          separator, sep="\n")
    quit()
else:
    print(separator,
          f"Welcome to the app, {user}.",
          "We have 3 texts to be analyzed.",
          separator, sep="\n")

# Vyber textu uzivatelem:
text_number = input("Enter a number btw. 1 and 3 to select: ")

# Overeni vyberu:
if not text_number.isdigit() or int(text_number) - 1 not in range(0, 3):
    print(separator,
          "Choice must be a whole number btw. 1 to 3.",
          "Terminating the program...",
          separator, sep="\n")
    quit()

# Rozdeleni slov a vytvoreni seznamu s nemi:
words = []

for word in TEXTS[int(text_number) - 1].split():
    words.append(word.strip(" -_.!?,"))

# Spocitani jednotlivych druhu slov a vypis uzivateli:
titlecase = 0
lowercase = 0
uppercase = 0
numeric = 0
numeric_sum = 0

for one_word in words:
    if one_word.istitle():
        titlecase += 1
    elif one_word.islower():
        lowercase += 1
    elif one_word.isupper():
        uppercase += 1
    elif one_word.isnumeric():
        numeric += 1
        numeric_sum = numeric_sum + int(one_word)
else:
    print(separator,
          f"There are {len(words)} words in the selected text.",
          f"There are {titlecase} titlecase words.",
          f"There are {uppercase} uppercase words",
          f"There are {lowercase} lowercase words",
          f"There are {numeric} numeric strings.",
          f"The sum of all the numbers is {numeric_sum}.",
          separator, sep="\n")

# Cetnosti delek slov:
occurences = {}

for length in words:
    if len(length) not in occurences:
        occurences[len(length)] = 1
    else:
        occurences[len(length)] += 1

# Graf cetnosti delek slov a jeho vypis:
print("LEN|    OCCURENCES    |NR. ",
      separator, sep="\n")
for key in sorted(occurences):
    stars = occurences[key] * "*"
    print(f"{key:>3}|{stars:<17} |{occurences[key]}",
          sep="\n")
else:
    print(separator)

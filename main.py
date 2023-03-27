#### HEAD ####
'''
1st_Project_ENGETO: první projekt do Engeto Online Python Akademie
author: Michal Eder
email: edermichal.eder@gmail.com
discord: Michal Eder#2018
'''
#### /HLAVICKA #####
#### ENTRY ####
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
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
users = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123", "pass123"]
users_passwords = dict(zip(users, passwords))
separator = "-"*60
#### /ENTRY ####
#### LOGIN ####
print(separator)
print(f'LOGIN'.center(60))
print('Please, enter your login credentials'.center(60))
print(separator)
user = input('User: ')
password = input('Password: ')
#### /LOGIN ####
#### LOGIN-CHECK ####
print(separator)
if user in users_passwords.keys() and password == users_passwords[user]:
    pass
else:
    print('INVALID USER OR PASSWORD'.center(60))
    print('TERMINATING PROGRAM'.center(60))
    input()
    quit()
##### /LOGIN-CHECK #####
print(f'Welcome to app, {user}')
print('We have three texts to analyze')
print(separator)
#### TEXT-CHOICE ####
text_choice = int(input('Enter number 1-3 to choose text for analysis: '))
if text_choice not in range(1,4):
    print('INVALID CHOICE'.center(60))
    print('TERMINATING PROGRAM'.center(60))
    input()
    quit()   
print(separator)
#### /TEXT-CHOICE ####
analyzed_text = (TEXTS[text_choice-1]).split()
analyzed_text_clear = [word.strip('.,?!:') for word in analyzed_text]
#print(analyzed_text_clear)
#WORD COUNT
word_len_category = dict()
title_case = 0
upper_case = 0
lower_case = 0
numeric = 0
numeric_sum = 0
for word in analyzed_text_clear:
    if len(word) in word_len_category.keys():
        word_len_category[len(word)] += 1
    else:
        word_len_category[len(word)] = 1
    if word.isalpha():
        if word.istitle():
            title_case += 1
        elif word.islower():
            lower_case += 1
        elif word.isupper():
            upper_case += 1
            title_case += 1
    elif word.isnumeric():
        numeric += 1
        numeric_sum += int(word)
#/WORD COUNT
#COUNT OUTPUT
print(f"""
There are {len(analyzed_text_clear)} words in the selected text.
There are {title_case} titlecase words.
There are {upper_case} uppercase words.
There are {lower_case} lowercase words.
There are {numeric} numeric strings.
The sum of all numbers is {numeric_sum}.
""")
#/COUNT OUTPUT

wlc_sorted = dict(sorted(word_len_category.items()))
print("LEN", "|".rjust(1),"OCCURENCES".center(20),"|".ljust(2),"NR.")
print("-"*35)
for key,value in wlc_sorted.items():
    print(
        (str(key).rjust(2)),
        ("|".rjust(2)),
        ("*"*value).ljust(20),
        ("|".ljust(1)),
        (str(value).rjust(3))
        )
input()

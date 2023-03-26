#### HLAVICKA ####
'''
1st_Project_ENGETO: první projekt do Engeto Online Python Akademie
author: Michal Eder
email: edermichal.eder@gmail.com
discord: Petr Svetr#4490
'''
#### /HLAVICKA #####
#### ZADANI ####
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
separator = "*"*60
#### /ZADANI ####
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
    print('INVALID LOGIN CREDENTIALS'.center(60))
    quit()
##### /LOGIN-CHECK #####
print(f'Welcome to app, {user}')
print('We have three texts to analyze')
print(separator)
#### TEXT-CHOICE ####
text_choice = int(input('Enter number 1-3 to choose text for analysis: '))
if text_choice not in range(1,3):
    print('INVALID CHOICE')
    quit()
else:
    pass
print(separator)
#### /TEXT-CHOICE ####
analyzed_text = (TEXTS[text_choice-1]).split()
analyzed_text_clear = [word.strip('.,?!:') for word in analyzed_text]
#print(analyzed_text_clear)

#počet slov
pocet_slov = 
#počet slov začínajících velkým písmenem,
#počet slov psaných velkými písmeny,
#počet slov psaných malými písmeny,
#počet čísel (ne cifer),
#sumu všech čísel (ne cifer) v textu


#analyza_textu


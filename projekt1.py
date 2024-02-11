"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Roman Loibl
email: r.Loibl@seznam.cz
discord: nathren.
"""
uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"}

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
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

separator = "-" * 40

jmeno = input("Zadej uživatelské jméno: ")
heslo = input("Zadej  heslo ")

if jmeno in uzivatele.keys() and heslo == uzivatele[jmeno]:
    print(f"""username: {jmeno}
password:{heslo}
{separator}
Welcome to the app, {jmeno}
We have {len(TEXTS)} texts to be analyzed.
{separator}""")
    #podmínka zda existuje text pro analyzování
    if len(TEXTS) == 0:
         print("Sorry, no text to analyze. Terminating the program..")
         exit()
else:
     print(f"""username: {jmeno}
password:{heslo}
unregistered user, terminating the program..""")
     exit()

cislo_textu = input(f"Enter a number btw. 1 and {len(TEXTS)} to select:")
print(separator)

# podmíínka pro kontrolu, zda uživatel nezadal neco jiného
if not cislo_textu.isnumeric() or int(cislo_textu) not in range(1,len(TEXTS) + 1):     
     print(f"Sorry, you didn't enter a number btw. 1 and {len(TEXTS)}. Terminating the program..")
     exit()

# slova spojena pomocí "-" nerozděluji protože je chápu jako jedno slovo např. buff-to-white
rozdeleny_text = TEXTS[int(cislo_textu)-1].split()
 
pocet_slov = len(rozdeleny_text)
pocet_slov_zac_velkym_pismenem = 0
pocet_slov_velkym_pismenem = 0
pocet_slov_malym_pismenem = 0
pocet_cisel = 0
suma_cisel = 0
delka_slov = []
cetnost_slov = {}

for slovo in rozdeleny_text:
    slovo = slovo.strip(".,!?") # zbavení se čárky a tečky pro jistotu predtím než se bude se slovem pracovat dál např. "155."
    delka_slov.append(len(slovo)) # vkládá délku slova do listu delka_slov
    if slovo[0].isupper(): # nepoužívám istitle kvuli možnosti mít ve slově i na jiném místě velké písmeno např. PhD
          pocet_slov_zac_velkym_pismenem += 1
    elif slovo.isupper():
         pocet_slov_velkym_pismenem += 1
    if slovo.islower():
         pocet_slov_malym_pismenem += 1
    if slovo.isnumeric():
         pocet_cisel += 1
         suma_cisel += int(slovo)
        
    
for delka_slova in sorted(delka_slov):
    if delka_slova not in cetnost_slov.keys():
     cetnost_slov[delka_slova] = delka_slov.count(delka_slova) # z listu delka slov vkladam do slovniku jako klíč a přiřazuju hodnotu podle četnosti dané délky slova

print(f"""There are {pocet_slov} words in the selected text.
There are {pocet_slov_zac_velkym_pismenem} titlecase words.
There are {pocet_slov_velkym_pismenem} uppercase words.
There are {pocet_slov_malym_pismenem} lowercase words.
There are {pocet_cisel} numeric strings.
The sum of all the numbers {suma_cisel}""")

max_delka_LEN = len(str(max(cetnost_slov.keys())))
max_delka_OCCURENCES = max(cetnost_slov.values())

#vytvaření grafu dle delek hodnot LEN a OCCURENCES s dynamickým ohraničením
print(separator)
print(f"LEN{' ' * (max_delka_LEN - len('LEN'))}|{'OCCURENCES':^{max_delka_OCCURENCES}}|NR.")
print(separator)
for key,index in cetnost_slov.items():    
    print(f"{' ' * (len('LEN') - len(str(key)))}{key}|{'*' * index}{' ' * (max_delka_OCCURENCES - index)}|{index}")     


  
        

meme_dict = {
    "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
    "LOL": "Częsta reakcja na coś zabawnego",
    "LMAO": "Częsta reakcja na coś bardzo zabawnego",
    "ROFL": "To samo co LMAO, ale jeszcze bardziej ekstremalne",
    "SMH": "Potrząsanie głową z dezaprobatą",
    "OMG": "Wyrażenie zdziwienia lub zdumienia",
    "WTF": "Wyrażenie zdziwienia, zdumienia lub oburzenia",
    "FTW": "Zwycięstwo, używane w pozytywnym kontekście",
    "TBH": "Do powiedzenia prawdy",
    "BRB": "Be Right Back, chwila przerwy",
    "IDK": "I Don't Know, nie wiem",
    "AFK": "Away From Keyboard, nieobecny przy klawiaturze",
    
}
# 0 chatgpt na pewno ręcznie zrobione   
   
while True:
    word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("To słowo nie zostało odnalezione w naszej bibliotece :(")

dizionario = {
    0 : 'A',
    1 : 'B',
    2 : 'C',
    3 : 'D',
    4 : 'E',
    5 : 'F',
    6 : 'G',
    7 : 'H',
    8 : 'I',
    9 : 'L',
    10: 'M',
    11: 'N',
    12: 'O',
    13: 'P',
    14: 'Q',
    15: 'R',
    16: 'S',
    17: 'T',
    18: 'U',
    19: 'V',
    20: 'Z'
    }

#print("Inserire parola da criptare:")
#parola = input()

ChiaveL = "ITISDELPOZZO"

while True:
    ChiaveN = []
    ParolaL = ""
    ParolaN = []
    ParolaCriptografataL = ""
    ParolaCriptografataN = []

    dizionarioInverso = {}

    for k,i in dizionario.items():
        dizionarioInverso[i] = k

    for k in ChiaveL.upper():
        ChiaveN.append(dizionarioInverso[k])

    print("\nInserire parola da criptografare >>>")
    ParolaL = input()
    if len(ParolaL) > len(ChiaveN):
        print("\nLa parola inserita è troppo lunga")
    else:
        for k in ParolaL.upper():
            ParolaN.append(dizionarioInverso[k])

        for k in range(0, len(ParolaN)):
            ParolaCriptografataN.append((ChiaveN[k] + ParolaN[k])%21)

        print(ParolaCriptografataN)

        for k in ParolaCriptografataN:
            ParolaCriptografataL = ParolaCriptografataL + dizionario[k]

        print(ParolaCriptografataL)
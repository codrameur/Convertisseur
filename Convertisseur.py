from Menu import*

def NbToConvert():
    while True:
        choix = input("quelle est le chiffre a convertir: ")
        try:
            choix = int(choix)
            return choix
        except:
            print("la valeur entré est mauvaise.\nVeuillez entré une nouvelle valeur.")
            continue

def BynaryToDecimal():
    
    choix_utilisateur=str(NbToConvert())
    print("vous avez choisi: %s" %(choix_utilisateur))
    results = 0
    for c in choix_utilisateur:
        results = results*2+int(c)
    print('----------------------------------------RESULTS----------------------------------------------')
    print("le nombre %s a pour notation binaire: %d" %(choix_utilisateur, results))
    print('----------------------------------------RESULTS----------------------------------------------')
        
    
def DecimalToBinary():
    
    choix_utilisateur=NbToConvert()
    choix = choix_utilisateur
    print("vous avez choisi: ", choix)
    results = ""
    while True:
        if choix%2:
            results = "1" + results
        else:
            results = "0" + results
        if choix//2 == 0:
            break
        choix = choix/2
    print('----------------------------------------RESULTS----------------------------------------------')
    print("le nombre %d a pour notation binaire: %s" %(choix_utilisateur, results))
    print('----------------------------------------RESULTS----------------------------------------------')


setting={
    "option":[
        {
            "name":"Binary to decimal",
            "launche":BynaryToDecimal
        },
        {
            "name":"Decimal to binary",
            "launche":DecimalToBinary
        }
    ]
       
}
menu_teste=Menu(setting)
menu_teste.run()
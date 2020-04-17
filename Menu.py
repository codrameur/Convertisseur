 
class Menu():
    def __init__(self,sett):    
        self.launche = True
        self.choix_utilisateur= ""
        self.sett=sett
    def run(self):
        launche=True
        while launche == True:
            print("------MENU------ \n")
            nb_option=0
            for x in self.sett["option"]:
                print(nb_option+1,"-",self.sett["option"][nb_option]["name"])
                nb_option += 1
            self.choix_utilisateur=input()

            try:
                self.choix_utilisateur=int(self.choix_utilisateur)
            except:
                print("vous avez choisi aucune option")
                continue


            self.sett["option"][self.choix_utilisateur-1]["launche"]()

            while launche==True:
                print("retourner au menu ? Y/N")
                choix_utilisateur=input()
                if choix_utilisateur=="Y":
                    break
                elif choix_utilisateur=="N":
                    launche=False
                else:
                    print("ereur")
                    continue
            print("\n \n \n")

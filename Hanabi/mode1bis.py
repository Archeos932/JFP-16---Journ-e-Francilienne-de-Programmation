import sys

def main():
    temps = 0
    moi = 0
    n = 0
    carte_joueur = [[],[],[]]

    
    for ligne in sys.stdin:
        donnees = ligne.split()
        if not donnees:
            continue

        commande = donnees[0]

        if commande == 'p':
            n = int(donnees[2])
            moi = int(donnees[3])
            temps = 0  
            
        elif commande == 't':
            j = int(donnees[1])
            if j == moi:
                temps += 1
                action = temps % 3
                
                if action == 0:
                    print("e 1")
                elif action == 1:
                    prochain_joueur = 1 + (moi % n)
                    print(f"I {prochain_joueur} A")
                elif action == 2:
                    print("d 1")
                
                sys.stdout.flush()
        elif commande == 'm' : 
                    num_joueur = 1
                    res = ""
                    for joueur in carte_joueur : 
                        if (num_joueur != moi) : 
                            res = res + str(num_joueur) + " m" 
                            for each_carte in joueur : 
                                res =res + " " + each_carte[0] + each_carte[1] 
                            res += "\n"
                        num_joueur +=1
                    print(res)


        elif commande == 'n' : 
            valeur = donnees[3]
            couleur = donnees[4]
            carte_joueur[int(donnees[1]) - 1].append([valeur , couleur ])

        elif commande == 'j' : 
            

        elif commande == 'f':
            code = int(donnees[1])
            if code == 0:
                break

if __name__ == "__main__":
    main()

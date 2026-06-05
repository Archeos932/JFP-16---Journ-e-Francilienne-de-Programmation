#!/usr/bin/env python3
import sys

def main():
    temps = 0
    moi = 0
    n = 0
    nbr_carte = 0
    carte_joueur = []
    info_carte_joueur = []

    for ligne in sys.stdin:
        donnees = ligne.split()
        if not donnees:
            continue

        commande = donnees[0]

        # --- Début de partie ---
        if commande == 'p':
            nbr_carte = int(donnees[1])
            n = int(donnees[2])
            moi = int(donnees[3])
            temps = 0  
            
            carte_joueur = [[0]*nbr_carte for _ in range(n)]
            info_carte_joueur = [[["?", "?"] for _ in range(nbr_carte)] for _ in range(n)]
            
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
       
        elif commande == 'm': 
            res_lignes = []
            for i in range(n):
                num_joueur = i + 1
                if num_joueur != moi:
                    cartes_formatees = []
                    for c in carte_joueur[i]:
                        if c == 0:
                            cartes_formatees.append("??")
                        else:
                            cartes_formatees.append(f"{c[0]}{c[1]}")
                    res_lignes.append(f"{num_joueur} m {' '.join(cartes_formatees)}")
            
            if res_lignes:
                print("\n".join(res_lignes))
                sys.stdout.flush()

        elif commande == 'r':
            res_lignes = []
            for i in range(n):
                cartes_str = " ".join([f"{c[0]}{c[1]}" for c in info_carte_joueur[i]])
                res_lignes.append(f"{i + 1} r {cartes_str}")
            
            if res_lignes:
                print("\n".join(res_lignes))
                sys.stdout.flush()

        elif commande == 'n': 
            num_joueur = int(donnees[1]) - 1
            position_carte = int(donnees[2]) - 1
            valeur = donnees[3]
            couleur = donnees[4]
            carte_joueur[num_joueur][position_carte] = [valeur, couleur]
            info_carte_joueur[num_joueur][position_carte] = ["?", "?"]

        elif commande == 'i': 
            joueur_valeur = int(donnees[1]) - 1
            valeur_valeur = donnees[2]
            for idx, bit in enumerate(donnees[3:]): 
                if bit == '1':
                    info_carte_joueur[joueur_valeur][idx][0] = valeur_valeur

        elif commande == 'I': 
            joueur_couleur = int(donnees[1]) - 1
            valeur_couleur = donnees[2]
            for idx, bit in enumerate(donnees[3:]): 
                if bit == '1':
                    info_carte_joueur[joueur_couleur][idx][1] = valeur_couleur

        #elif commande == 'j' :

        elif commande == 'f':
            code = int(donnees[1])
            if code == 0:
                break

if __name__ == "__main__":
    main()
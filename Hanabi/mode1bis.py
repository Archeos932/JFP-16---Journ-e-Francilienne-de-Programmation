#!/usr/bin/env python3
import sys

def main():
    temps = 0
    moi = 0
    n = 0
    carte_joueur = []

    for ligne in sys.stdin:
        donnees = ligne.split()
        if not donnees:
            continue

        commande = donnees[0]

        if commande == 'p':
            nbr_carte = int(donnees[1])
            n = int(donnees[2])
            moi = int(donnees[3])
            temps = 0  
            
            # Initialisation des cartes à chaque nouvelle partie
            carte_joueur = [[0]*nbr_carte for _ in range(n)]
            
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
            for i, joueur in enumerate(carte_joueur):
                num_joueur = i + 1
                if num_joueur != moi:
                    cartes_connues = [f"{c[0]}{c[1]}" for c in joueur if c != 0 and c != ['?', '?']]
                    
                    if cartes_connues:
                        res_lignes.append(f"{num_joueur} m {' '.join(cartes_connues)}")
            
            if res_lignes:
                print("\n".join(res_lignes))
                sys.stdout.flush()

        elif commande == 'n': 
            num_joueur = int(donnees[1]) - 1
            position_carte = int(donnees[2]) - 1
            valeur = donnees[3]
            couleur = donnees[4]
            carte_joueur[num_joueur][position_carte] = [valeur, couleur]

        elif commande == 'f':
            code = int(donnees[1])
            if code == 0:
                break

if __name__ == "__main__":
    main()
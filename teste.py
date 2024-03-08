from base import BOOSTER_DICT,B_DECR,B_INCR


texte = [['bienvenue', 'enfant'], ['être', 'pas','peu','joli']]
resultat = [['bienvenue', 2.0]], [['peu', 0],['joli', 2.2]]


def booster(texte,resultat):

    for i,combine in enumerate(texte):
        

        for mot in combine:

            if mot in BOOSTER_DICT.keys():


                if BOOSTER_DICT[mot] == B_INCR:         # Verifie si la value du booster est +


                    for liste in resultat:       

                        for i,tuplet in enumerate(liste):

                                if tuplet[0] == mot:        #trouvé le boosteur
                                    liste[i+1][1]*= B_INCR
                                    print(liste)


                elif BOOSTER_DICT[mot] == B_DECR:

                    for liste in resultat:      

                        for i,tuplet in enumerate(liste):

                                if tuplet[0] == mot:
                                    liste[i+1][1]*= B_DECR
                                    print(liste)
    return resultat
        

print(booster(texte,resultat))






                        
                            


            

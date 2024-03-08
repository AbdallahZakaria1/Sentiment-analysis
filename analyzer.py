import lemmatizer
from base import BOOSTER_DICT, POLARITY, B_DECR, B_INCR

NEGATE = ["pas", "jamais", "plus", "rien", "beaucoup","nullement", "sans", "ni"]


def analyzer(text):

    texte = lemmatizer.lemmatize(text)

    resultat = []

    liste34 = []

    for ligne in texte:
        t = []
        b = 0


        for i,mot in enumerate(ligne):
            if mot in POLARITY:

                t.append([mot, POLARITY[mot]])

                if ligne[i-1] in NEGATE:
                    t[-1][1] *= -1

                try:
                    if ligne[i-2] in NEGATE:
                        t[-1][1] *= -1
                except:pass

                if mot in BOOSTER_DICT:
                    t[-1][1] = 0
            
                try : 
                    if ligne[i-2] in BOOSTER_DICT.keys():
                        if BOOSTER_DICT[ligne[i-2]] == B_INCR:
                            t[-1][1] *= B_INCR
                        elif BOOSTER_DICT[ligne[i-2]] == B_DECR:
                            t[-1][1] *= B_DECR
                except:pass

                if ligne[i-1] in BOOSTER_DICT.keys():
                    if BOOSTER_DICT[ligne[i-1]] == B_INCR:
                        t[-1][1] *= B_INCR
                    elif BOOSTER_DICT[ligne[i-1]] == B_DECR:
                        t[-1][1] *= B_DECR

            if mot not in POLARITY:
                t.append([mot, 0])

            
            b += t[-1][1]
            
        if t:
            resultat.append(t)
            eq = b/len(t)
            liste34.append(eq)
    b = sum(liste34)


    eq_final_combine_moyenne = b/len(liste34) if len(liste34) > 0 else 0

    print(eq_final_combine_moyenne)
    return str(get_sentiment(eq_final_combine_moyenne)) + " avec une polarité de : " + str(eq_final_combine_moyenne)

def get_sentiment(score):
    if score >= 0.3:
        return 'positive'
    elif score <= -0.3:
        return 'negative'
    else:
        return 'neutre'

print(analyzer("je suis meilleur que toi"))



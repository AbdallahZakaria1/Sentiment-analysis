import re
from base import POLARITY, mot_connu, BOOSTER_DICT, stop_words

# Cette fonction permet de nettoyer le texte

def nettoyer_text(text):

    # On crée une variable vide pour la phrase "nettoyée"

    resultat = ""

    # r'(\S+|\s+)' permet de récupérer les mots et les espaces

    # Différence avec split = garde les espaces

    for mot in re.findall(r"(\S+|\s+)", text):

        # On veut tous les mots connus, et les apostrophes afin de les analyser

        if mot not in POLARITY or mot not in mot_connu or mot.lower() not in mot_connu or mot not in BOOSTER_DICT or mot.lower() not in BOOSTER_DICT:
                for lettre in mot:
                    if lettre.isalnum() == False:
                        if lettre == "'":
                            resultat += " "
                        else:
                            resultat += " " + lettre.lower() + " "
                    else:
                        resultat += lettre.lower()
        else:
            resultat += mot

    # permet de séparer les mots par des espaces

    text = resultat.split()

    # On supprime les mots inutiles

    for i,mot in enumerate(text):
        if text[i-1] + " " + mot in BOOSTER_DICT:
            text[i] = text[i-1] + " " + mot
            text.remove(text[i-1])
    
    for mot in text:
        if mot in stop_words:
            if mot not in BOOSTER_DICT or mot not in mot_connu:
                pos = text.index(mot)
                text.remove(text[pos])

    # On supprime les mots qui commencent par # ou @

    text = " ".join([mot for mot in text if not mot.startswith("#") and not mot.startswith("@")])

    # on renvoie le texte "nettoyé"
    return text

# on separe le texte nettoyé en phrases et mots a partir des virgules


def split(text):

    text = nettoyer_text(text)
    
    # diviseur with regex
    diviseur = re.split(r'[,;:!?.]', text)


    textsplit = []

    for partie in diviseur:
        
        textsplit.append(partie.split())

    for ligne in textsplit:

        for i,mot in enumerate(ligne):
            if ligne[i-1] + " " + mot in BOOSTER_DICT:
                ligne[i] = ligne[i-1] + " " + mot
                ligne.remove(ligne[i-1])
                
    return textsplit

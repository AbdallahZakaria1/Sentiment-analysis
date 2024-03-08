import tokenizer
from base import lefff, BOOSTER_DICT


def lemmatize(text):

    text = tokenizer.split(text)

    for ligne in text:

        if len(ligne) == 0:
            text.remove(ligne)

        for mot in ligne:
            if mot not in BOOSTER_DICT.keys():
                try:
                    pos = ligne.index(mot)
                    ligne[pos] = lefff[mot]
                except:pass

    return text
import json 
import urllib.request

B_INCR = 1.5
B_DECR = 0.5

BOOSTER_DICT = \
    {"absolument": B_INCR, "ainsi": B_INCR, "archi": B_INCR, "beaucoup": B_INCR,
     "bigrement": B_INCR, "bougrement": B_INCR, "carrément": B_INCR, "complètement": B_INCR,
     "considérablement": B_INCR, "davantage": B_INCR, "diablement": B_INCR, "diantrement": B_INCR,
     "divinement": B_INCR, "drôlement": B_INCR, "délicieusement": B_INCR, "entièrement": B_INCR,
     "exceptionnel": B_INCR, "exceptionnelle": B_INCR, "exceptionnellement": B_INCR, "exceptionnelles": B_INCR,
     "exceptionnels": B_INCR, "excessivement": B_INCR, "extra": B_INCR, "extrême": B_INCR,
     "extrêmement": B_INCR, "fabuleusement": B_INCR, "fichtrement": B_INCR, "fort": B_INCR,
     "forte": B_INCR, "fortes": B_INCR, "forts": B_INCR, "grandement": B_INCR,
     "hyper": B_INCR, "impeccablement": B_INCR, "incroyablement": B_INCR, "infiniment": B_INCR,
     "joliment": B_INCR, "merveilleusement": B_INCR, "prodigieusement": B_INCR, "profondément": B_INCR,
     "putain de": B_INCR, "rudement": B_INCR, "sacrément": B_INCR, "spécialement": B_INCR,
     "sublimement": B_INCR, "super": B_INCR, "superbement": B_INCR, "tant": B_INCR,
     "tellement": B_INCR, "terriblement": B_INCR, "totalement": B_INCR, "trop": B_INCR,
     "très": B_INCR, "ultra": B_INCR, "vachement": B_INCR, "vraiment": B_INCR,
     "énormément": B_INCR, "approximativement": B_DECR, "assez": B_DECR, "difficilement": B_DECR,
     "environ": B_DECR, "guère": B_DECR, "insuffisament": B_DECR, "insuffisamment": B_DECR,
     "juste": B_DECR, "léger": B_DECR, "légers": B_DECR, "légère": B_DECR,
     "légèrement": B_DECR, "légères": B_DECR, "moins": B_DECR, "peu": B_DECR,
     "plutôt": B_DECR, "presque": B_DECR, "quasi": B_DECR, "quasiment": B_DECR,
     "quelque": B_DECR, "quelque peu": B_DECR, "rare": B_DECR, "rarement": B_DECR,
     "à peine": B_DECR, "à peu près": B_DECR}

NEGATE = ["pas", "jamais", "plus", "rien", "beaucoup","nullement", "sans", "ni"]

lefff = {}

with open('data\lefff-3.4.mlex', encoding = 'utf-8', mode ='r') as data:
    try:
        for donnee in data:
            parties = donnee.split('\t')
            lefff[parties[0]] = parties[2]
    except:pass

POLARITY = {}

with open('data/lexicon.txt', 'r', encoding='utf-8') as lexicon:
    for ligne in lexicon:
        fields = ligne.strip().split('->')
        POLARITY[fields[0]] = float(fields[1])

mot_connu = []

# Lexique des Formes Fléchies du Français (Lefff)
with open('data\lefff-3.4.mlex', encoding = 'utf-8', mode ='r') as leff:
    try:
        for ligne in leff:
            fields = ligne.split('\t')
            mot_connu.append(fields[0])
    except:pass

stop_words_url = "https://raw.githubusercontent.com/elevesabri/mots_inutile/main/stop_word.json"
with urllib.request.urlopen(stop_words_url) as f:
    stop_words = json.load(f)
from pattern.fr import sentiment

# Texte à analyser
texte = ''' je suis meilleur que toi '''

# Analyse de sentiment
polarity = sentiment(texte)[0]

# Affichage des résultats
print("Polarité: ", polarity)
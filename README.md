# Qu'est-ce que l'analyse de sentiments ?

L'analyse de sentiments est un processus informatique qui permet de déterminer les émotions et attitudes d'un individu à l'égard d'un sujet ou d'un produit en analysant les données textuelles.

Cela peut être utilisé pour comprendre les réactions des consommateurs à un produit ou à une marque, ou pour évaluer les opinions d'un public sur un sujet donné.

##  Les etape de notre Projet :
# 1. Lemmatize
Il permet de "nettoyer" notre phrase modifiant les mots par des mots connu par exemple connu -> connaitre
#2. Tokenizer
On met la phrase sous forme de token afin de supprimer les mots inutiles, ou inconnu
#3. Analyser
On va analyser la phrase en la "nettoyant", on va calculer la polarité de chaque mots puis faire une "moyenne" avec des booster
# LEFFF

Le Lefff est un lexique libre et gratuit pour la reconnaissance de la langue naturelle en français,
utilisé pour des tâches comme la génération de textes et le traitement automatique du langage,
il est maintenu par une communauté de contributeurs bénévoles.

Retrouvé dans [Benoît Sagot Webpage about LEFFF](http://alpage.inria.fr/~sagot/lefff-en.html)

Pour ce projet il nous sert pour retrouver la forme original d'un mot. Je vous renvoie vers Lemmatizer

[LEFFF download hyperlink](https://gforge.inria.fr/frs/download.php/file/34601/lefff-3.4.mlex.tgz)

#Lexicon
Notre "lexicon" vient de Vader-Sentiment.
Il permet de recuperer la polarité d'un mot connu

#Stop word
Il nous permet de retirer les mots inutile.
Dans notre cas il servira a réduire le nombre de mots à "analyser" car on en fait une moyenne.
[Ressource](https://countwordsfree.com/stopwords/french)

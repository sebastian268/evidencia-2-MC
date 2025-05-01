import nltk
from nltk import CFG
nltk.download('punkt')

grammar = CFG.fromstring("""
oracion -> sujeto verbo oracion_p
oracion_p -> objeto
oracion_p -> 

sujeto -> frase_nominal
objeto -> frase_nominal

frase_nominal -> frase_nominal_inicial frase_nominal_p

frase_nominal_inicial -> determinante sustantivo adjetivo
frase_nominal_inicial -> sustantivo frase_nominal_s_p
frase_nominal_inicial -> pronombre

frase_nominal_s_p -> adjetivo
frase_nominal_s_p -> 

frase_nominal_p -> conjuncion frase_nominal
frase_nominal_p -> 

verbo -> raiz_verbal sufijo_verbal

raiz_verbal -> "jagon" | "vāedar" | "kēliar" | "rhaenagon" | "drējelagon"
sufijo_verbal -> "i" | "is" | "ir" | "ion"

determinante -> "ābra" | "ziry" | "bisy" | "morys" | "velg" | "līr" | "tīr"
sustantivo -> "valzȳrys" | "zaldrīzes" | "azantys" | "qintir" | "voktys" | "melos" | "dūri" | "rhaegon"
adjetivo -> "sȳz" | "hāedar" | "zȳhon" | "velos" | "rhaeshisar" | "zalar" | "sūngar"
pronombre -> "nyke" | "ao" | "zȳhon" | "ses" | "til" | "ōs"
conjuncion -> "vose" | "lōr" | "se"
""")

parser = nltk.ChartParser(grammar)

sentence = "die Hund und Mark spielt Fußball sehr gut . ich spielt nicht gut . "

tokens = nltk.word_tokenize(sentence)

for tree in parser.parse(tokens):
    tree.pretty_print()

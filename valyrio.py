import nltk
from nltk import CFG



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

raiz_verbal -> "jagon"
raiz_verbal -> "vaedar"
raiz_verbal -> "keliar"
raiz_verbal -> "rhaenagon"
raiz_verbal -> "drejelagon"

sufijo_verbal -> "i"
sufijo_verbal -> "is"
sufijo_verbal -> "ir"
sufijo_verbal -> "ion"

determinante -> "abra"
determinante -> "ziry"
determinante -> "bisy"
determinante -> "morys"
determinante -> "velg"
determinante -> "lir"
determinante -> "tir"

sustantivo -> "valzyrys"
sustantivo -> "zaldrizes"
sustantivo -> "azantys"
sustantivo -> "qintir"
sustantivo -> "voktys"
sustantivo -> "melos"
sustantivo -> "duri"
sustantivo -> "rhaegon"

adjetivo -> "syz"
adjetivo -> "haedar"
adjetivo -> "zyhon"
adjetivo -> "velos"
adjetivo -> "rhaeshisar"
adjetivo -> "zalar"
adjetivo -> "sungar"

pronombre -> "nyke"
pronombre -> "ao"
pronombre -> "zyhon"
pronombre -> "ses"
pronombre -> "til"
pronombre -> "os"

conjuncion -> "vose"
conjuncion -> "lor"
conjuncion -> "se"
""")

parser = nltk.ChartParser(grammar)

tokens = ["nyke", "jagon", "is", "azantys", "syz"]

for tree in parser.parse(tokens):
    tree.pretty_print()

trees = list(parser.parse(tokens))
print(f"Número de árboles: {len(trees)}")

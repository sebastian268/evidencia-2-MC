import nltk
from nltk import CFG
nltk.download('punkt')

grammar = CFG.fromstring("""
oración → sujeto verbo oración'
oración' → objeto
oración' → 

sujeto → frase_nominal

objeto → frase_nominal

frase_nominal → frase_nominal_inicial frase_nominal'

frase_nominal_inicial → determinante sustantivo adjetivo
frase_nominal_inicial → sustantivo frase_nominal_s'
frase_nominal_inicial → pronombre

frase_nominal_s' → adjetivo
frase_nominal_s' → 

frase_nominal' → conjunción frase_nominal
frase_nominal' → 

verbo → raíz_verbal sufijo_verbal

raíz_verbal → "jagon"
raíz_verbal → "vāedar"
raíz_verbal → "kēliar"
raíz_verbal → "rhaenagon"
raíz_verbal → "drējelagon"

sufijo_verbal → "i"
sufijo_verbal → "is"
sufijo_verbal → "ir"
sufijo_verbal → "ion"

determinante → "ābra"
determinante → "ziry"
determinante → "bisy"
determinante → "morys"
determinante → "velg"
determinante → "līr"
determinante → "tīr"

sustantivo → "valzȳrys"
sustantivo → "zaldrīzes"
sustantivo → "azantys"
sustantivo → "qintir"
sustantivo → "voktys"
sustantivo → "melos"
sustantivo → "dūri"
sustantivo → "rhaegon"

adjetivo → "sȳz"
adjetivo → "hāedar"
adjetivo → "zȳhon"
adjetivo → "velos"
adjetivo → "rhaeshisar"
adjetivo → "zalar"
adjetivo → "sūngar"

pronombre → "nyke"
pronombre → "ao"
pronombre → "zȳhon"
pronombre → "ses"
pronombre → "til"
pronombre → "ōs"

conjunción → "vose"
conjunción → "lōr"
conjunción → "se"

""")

parser = nltk.ChartParser(grammar)

sentence = '"nyke" "jagon" "is" "azantys" "sȳz"'

tokens = nltk.word_tokenize(sentence)

for tree in parser.parse(tokens):
    tree.pretty_print()

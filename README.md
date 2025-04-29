# evidencia-2-MC

# Sebastián Acosta Marín 
# A01278278

Una gramática en programación es un conjunto formal de reglas que definen cómo se pueden construir expresiones válidas dentro de un lenguaje. Estas gramáticas son fundamentales en el diseño de lenguajes de programación, ya que de esta manera se construyen lo que son los compiladores, ya que gracias a estos se puede describir de una mejro manera la sintaxis que debe seguir el código para ser comprendido y procesado correctamente por una máquina.
Un pequeño y simple ejemplo de lo que puede ser considerado como una gramatica funcional 
```bnf
oración    -> sujeto verbo objeto
sujeto     -> "Juan" | "María"
verbo      -> "come" | "lee"
objeto     -> "manzanas" | "libros"
```

Esta grámatica hacepta frases como: 
- Juan come manzanas
- Maria lee libros
- Maria come libros

Para este proyecto usare un parser para indentificar si la palabra pertenece o no pertenece a la gramatica establecida el cual es conocido como parserLL(1), el cual solo sirve para analizar lo que vienen siendo gramaticas libres de contexto. Este parser analiza las entradas de izquierda a derecha, pero para que este parser pueda funcionar se necesita que la gramatica cumpla las siguientes dos reglas:

- Que la gramatica no tenga ambigüedad
- Que la gramtica no tenga recursión hacia a izquierda

Un ejmeplo pequeño en donde existe una grámatica con ambigüedad es la siguiente:

```bnf
oración   -> oración conjunción oración
           | palabra

palabra   -> "llora" | "rie"
conjunción -> "y"
```

La ambigüedad se da debido a que hay más de una manera de crear la misma frase, por lo que el parser no sabe que camino tomar y falla.

La recursión hacia la izquierda se da cuando un elemento de la gramatica se llama asi mismo hasta la izquierda, lo cual provoca una recursión hacia la izquierda de manera constante.
```bnf
lista  -> lista "," elemento
        | elemento

elemento -> "a" | "b" | "c"
```
En este pequeño ejemplo la recursividad hacia la iquierda se encuentra en la siguiente linea:

```bnf
lista -> lista "," elemento
```

# Lenguaje elegido 

El lenguaje que elegí para escribir una pequeña gramatica es el "alto valyrio" el cual es el lenguaje hablado por la familia targaryen en los famosos libros de "A song of ice and fire" (el cual puede ser aprendido en la plataforma de Duolingo por cierto)

La gramatica que establecí es la siguiente:

```bnf
oración        -> sujeto verbo objeto
                | sujeto verbo
                | sujeto "issi"

sujeto         -> frase_nominal
objeto         -> frase_nominal

frase_nominal  -> frase_nominal conjunción frase_nominal
                | determinante sustantivo adjetivo
                | determinante sustantivo
                | sustantivo adjetivo
                | sustantivo
                | pronombre

verbo          -> raíz_verbal sufijo_verbal

raíz_verbal    -> "jagon" | "vāedar" | "kēliar" | "rhaenagon" | "drējelagon"
sufijo_verbal  -> "i" | "is" | "ir" | "ion"

determinante   -> "ābra" | "ziry" | "bisy" | "morys" | "velg" | "līr" | "tīr"
sustantivo     -> "valzȳrys" | "zaldrīzes" | "azantys" | "qintir" | "voktys" | "melos" | "dūri" | "rhaegon"
adjetivo       -> "sȳz" | "hāedar" | "zȳhon" | "velos" | "rhaeshisar" | "zalar" | "sūngar"
pronombre      -> "nyke" | "ao" | "zȳhon" | "ses" | "til" | "ōs"
conjunción     -> "vose" | "lōr" | "se"
```

Pero el problema de esta gramatica es que cuenta tanto con ambigüedad como con recursión en la izquierda:

Recursividad hacia la izquiera 

```bnf
frase_nominal  -> frase_nominal conjunción frase_nominal
```

Aquí en esta parte de la gramática existe lo que es la recursividad hacia la izquierda debido a que el elemento "frase_nominal" se llama a si mismo desde la izqueirda, lo cual podría generar un ciclo infinito hacia la izquierda si no se maneja de la manera correcta, lo cual imposibilita el uso del parser LL(1)

Además la ambigüedad se encuentra en la siguiente linea de la gramatica:

```bnf
oración        -> sujeto verbo objeto
                | sujeto verbo
                | sujeto "issi"
```





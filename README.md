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



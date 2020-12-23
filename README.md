# API MELI
## api_mutantes

## Stack
- Flask 
- Insomnia (para hacer los requests)
- Python 3
- Postgres
- Pytest

## CLONAR REPOSITORIO
Posicionarse por consola en la carpeta donde quiera clonarse el repositorio y escribir.
>>> git clone


Se hosteó la API en Heroku, la cual detecta a través de una secuencia de ADN si el humano es MUTANTE o no. Lo hace a través de un programa donde 
busca secuencias de 4 letras iguales ya se de forma vertical, horizontal o diagonal.

## NUBE
LINK API:  https://apimutantesnodb.herokuapp.com/

## ENDPOINT (MUTANT):
https://apimutantesnodb.herokuapp.com/mutant/<adn>

En este endpoint debe introducirse mediante el método HTTP POST un json con una cadena de ADN que tenga el siguiente formato:

{
  'dna':["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
}

En el caso de que sea mutante la API devuelve un STATUS_CODE de 200 y un mensaje diciendo: "Es mutante".

En caso de que no lo sea, pone un mensaje "no es mutante" y devuelve un error 403-Forbidden.


## TESTS

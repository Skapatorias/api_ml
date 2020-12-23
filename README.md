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
>>> git clone https://github.com/Skapatorias/api_ml.git


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
Se debe tener instalado Pytest y Coverage (pip install pytest coverage)
#### Por consola, en la carpeta raíz, ejecutar el comando "pytest". Se ejecutarán los TEST y se verá el resultado.
>>> pytest

logica_test.py .........                                                                                                                                         [100%]

========================================================================== 9 passed in 0.09s =======================================================================

#### Con el comando "coverage report" veremos la cobertura de pruebas
>>> coverage report


#### Para ver un html más detallado con los resultados, escribir en consola:
>>> coverage html

Se creará una carpeta llamada htmlcov. Allí dentro abrir el archivo "index.html" y se verán los datos en formato HTML.







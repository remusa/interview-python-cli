# Python CLI

## Instrucciones

* Se necesitará `Python3` (se probó con versión `3.8.5`).

* Llamar la CLI usando el comando `python cli.py`.
  * Se preguntarán los argumentos en caso de que no hayan sido pasados.

```python
>> python cli.py
>> Límite superior:
100
>> Límite inferior:
20
>> Objetivo:
52.5
>> Error:
0.05
```

* Para llamar la CLI pasando argumentos usar el comando de la sig. manera: `python cli.py [limite_superior] [limite_inferior] [objetivo] [error]`
  * Ejemplo: `python cli.py 100 20 52.5 0.05`

* Si los argumentos son números válidos, se regresará el resultado de la sig. manera:

```python
# llamada
>> python cli.py 100 20 52.5 0.05

# resultado
>> Resultado: 52.5 | Iteraciones: 5
```

## Instructions

* `Python3` needed (tested with version `3.8.5`).
* Use the following command to call the CLI: `python cli.py`.
  * Arguments will be asked for in case they weren't provided.

```python
>> python cli.py
>> Límite superior:
100
>> Límite inferior:
20
>> Objetivo:
52.5
>> Error:
0.05
```

* Pass arguments to the CLI in the following manner: `python cli.py [superior_limit] [inferior_limit] [objective] [error]`
  * Ejemplo: `python cli.py 100 20 52.5 0.05`

* If arguments are valid numbers, the CLI will return the result along with the number of iterations it took to get in the following manner:

```python
# call
>> python cli.py 100 20 52.5 0.05

# result
>> Resultado: 52.5 | Iteraciones: 5
```

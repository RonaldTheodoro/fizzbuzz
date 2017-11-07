"""
Regras do Fizzbuzz

1. Se posição for multipla de 3: fizz
2. Se posição for multipla de 5: buzz
3. Se posição for multipla de 3 e 5: fizzbuzz
4. Para qualquer outra posição fale o proprio Nº.
"""


from functools import partial

multiple_of = lambda base, num: num % base == 0
multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)


def robot(number):
    if multiple_of_3(number) and multiple_of_5(number):
        return 'fizzbuzz'

    elif multiple_of_5(number):
        return 'buzz'
   
    elif multiple_of_3(number):
        return 'fizz'
    return str(number)

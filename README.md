Problem:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89,...

Considerando os termos da sequência de Fibonacci cujos valores não excedem quatro milhões, encontre a soma dos termos de valor par

Explicando o código:

A função fibonacci(n) recebe um número n como argumento e retorna a sequência de Fibonacci com os valores menores que n.

A função inicia a lista com os dois primeiros valores da sequência de Fibonacci ([1, 2]) e a atualiza até que o último valor seja menor que n.

A função retorna a lista resultante, mas exclui o último valor, já que ele é maior que n.

Na linha soma = sum([x for x in fibonacci(4000000) if x % 2 == 0]), a função fibonacci() é chamada com o argumento 4000000 para obter a sequência de Fibonacci cujos valores não excedem quatro milhões. Em seguida, é feita uma lista por compreensão para selecionar apenas os valores pares da sequência, e a soma desses valores é calculada com a função sum().

Por fim, o resultado é impresso com a função print().

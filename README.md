# AnagramasPrimos
AnagramasPrimos é um meio probabilístico de obter alguns números primos após um número primo dado.

# Conceito base
Pega-se uma lista de números primos, calcula-se todos os anagramas de cada um dessa lista, após isso se remove os repetidos. Os anagramas que sobram passam por um teste de primalidade, onde alguns serão primos e outros não.

# Uso básico
'var' é a lista de anagramas que são primos.
'n1', 'n2', 'n3' e 'n4' são respectivamente a mantissa, expoente (base 10), valor a ser somado com o número obtido entre 'n1' e 'n2', e o número máximo de primos a ser retornado dentre os que foram achados, podendo retornar menos primos que o especificado.

var = call_fases(n1, n2, n3, n4)

print(var)

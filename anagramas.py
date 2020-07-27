# -*- coding: utf-8 -*-
from itertools import permutations
import random, tqdm

def anagrama(var1):
	"""
	Transforma 'var1' em string e calcula os anagramas.
	"""
	k = [''.join(anagrama) for anagrama in permutations(str(var1))]
	return k

def miller_rabin(n, k=100):
	"""
	n = número a ser testado.\n
	k = número de repetições do teste.
	"""
	if n == 2:
		return True
	if n%2 == 0:
		return False
	r, s = 0, n - 1
	while s%2 == 0:
		r += 1
		s //= 2

	for _ in range(k):
		a = random.randrange(2, n - 1)
		x = pow(a, s, n)
		if x == 1 or x == n - 1:
			continue
		for _ in range(r - 1):
			x = pow(x, 2, n)
			if x == n - 1:
				break
		else:
			return False
	return True

def fase1(mantissa, expoente, n_soma):
	"""
	Implementação da 'fase1' com os valores passados.
	"""
	t1 = int(mantissa*pow(10, expoente)) + 1
	t2 = t1 + n_soma

	primos = []
	for i0 in tqdm.tqdm(range(t1, t2, 2), desc='  Calculando primos no intervalo ({}, {})'.format(t1, t2)):
		if i0%5 == 0:
			pass
		else:
			if (miller_rabin(i0, 100)) == True:
				primos.append(i0)
			else:
				pass

	l3 = []
	for i2 in tqdm.tqdm(primos, desc='  Pegando os anagramas > {}'.format(primos[-1])):
		fr = list(set(anagrama(i2)))
		for ft in fr:
			ift = int(ft)
			if ift not in l3:
				if ift > primos[-1]:
					l3.append(ift)
				else:
					pass
	return l3

def fase2(jk, n=5):
	"""
	Implementação da 'fase2' com a saída da 'fase1' após ser removidos os repetidos.
	"""
	dc = {}
	for p in tqdm.tqdm(jk, desc='  Testando anagramas'):
		if len(dc) < n:
			if (miller_rabin(p, 100)) == True:
				dc[str(jk.index(p) + 1)]=p
			else:
				pass
		else:
			break

	fg = []
	try:
		for k in dc:
			fg.append(dc[k])
	except IndexError:
		pass
	return fg

def call_fases(mantissa, expoente, n, n_soma=100):
	"""
	Chamada das funções principais.
	"""
	var1 = fase1(mantissa, expoente, n_soma)
	var2 = list(set(var1))
	var3 = fase2(var2, n)
	print('  Número de anagramas:                {}'.format(len(var1)))
	print('  Número de anagramas sem repetições: {}'.format(len(var2)))
	print('  Número de primos encontrados:       {}'.format(len(var3)))
	print('  Porcentagem de primos (%):          {}'.format('%.4f'%(100 * (len(var3)/len(var2)))))
	var3.sort()
	return var3

# Chamada de exemplo
if '__main__' == __name__:
	mantis = 1	# mantissa básica
	exp = 5		# expoente para base 10
	n_max_primos = 10000	# número máximo de primos a serem retornados, podendo ser menor o número retornado
	n_sum = 1000	# número a ser somado com o número gerado pela mantissa e expoente
	var = call_fases(mantis, exp, n_max_primos, n_sum)
	if len(var) > 0:
		print('  Menor primo encontrado:             {}'.format(var[0]))
		print('  Maior primo encontrado:             {}'.format(var[-1]))
	else:
		print('  Nenhum primo encontrado!')

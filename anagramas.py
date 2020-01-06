# -*- coding: utf-8 -*-
from itertools import permutations
import random

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

def remove_repetidos(lista):
	"""
	Remove os anagramas iguais.
	"""
	l = []
	for i in lista:
		if i not in l:
			l.append(i)
		else:
			pass
	l.sort()
	return l

def fase1(mantissa, expoente, n_soma):
	"""
	Implementação da 'fase1' com os valores passados.
	"""
	t1 = int(mantissa*pow(10, expoente)) + 1
	t2 = t1 + n_soma

	primos = []
	for i0 in range(t1, t2, 2):
		if i0%5 == 0:
			pass
		else:
			if (miller_rabin(i0, 100)) == True:
				primos.append(i0)
			else:
				pass

	l3 = []
	for i2 in primos:
		fr = anagrama(i2)
		for ft in fr:
			if (int(ft)) > primos[-1]:
				l3.append(int(ft))
			else:
				pass
	return l3

def fase2(jk, n=5):
	"""
	Implementação da 'fase2' com a saída da 'fase1' após ser removidos os repetidos.
	"""
	jk.sort(reverse=True)
	dc = {}
	for p in jk:
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

def call_fases(mantissa, expoente, n_soma=100, n=5):
	"""
	Chamada das funções principais.
	"""
	var1 = fase1(mantissa, expoente, n_soma)
	var2 = remove_repetidos(var1)
	var3 = fase2(var2, n)
	var3.sort()
	return var3

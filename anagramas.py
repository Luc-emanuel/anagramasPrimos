# -*- coding: utf-8 -*-
from itertools import permutations
import random

"""
Script simples, sem necessidade no momento de uso de classes.
"""

def anagrama(var1):
	"""
	Transforma 'var1' em string e calcula os anagramas.
	"""
	k = [''.join(anagrama) for anagrama in permutations(str(var1))]
	return k

def miller_rabin(n, k=100):
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

def fase1(f0, f1, f2):
	"""
	Implementação da 'fase1' com os valores passados.
	"""
	t1 = int(f0*(10**f1)) + 1
	t2 = t1 + f2

	p1 = []
	for i0 in range(t1, t2, 2):
		if i0%5 == 0:
			pass
		else:
			p1.append(i0)

	primos = []

	for u1 in p1:
		if (miller_rabin(u1, 100)) == True:
			primos.append(u1)
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

def fase2(jk):
	"""
	Implementação da 'fase2' com a saída da 'fase1' após ser removidos os repetidos.
	"""
	dc = {}
	for p in jk:
		if (miller_rabin(p, 100)) == True:
			dc[str(jk.index(p) + 1)]=p
		else:
			pass

	fg = []
	try:
		for k in dc:
			fg.append(dc[k])

	except IndexError:
		pass
	return fg

def call_fases(x, y, z=200):
	"""
	Chamada das funções principais.
	"""
	var1 = fase1(x, y, z)
	var2 = remove_repetidos(var1)
	var3 = fase2(var2)
	return var3

# -*- coding: utf-8 -*-
from itertools import permutations

def anagrama(var1):
	"""
	Transforma 'var1' em string e calcula os anagramas.
	"""
	k = [''.join(anagrama) for anagrama in permutations(str(var1))]
	return k

def teste_primalidade(var1):
	"""
	Verifica se determinado é composto ou não.
	"""
	y, l1 = int(var1**(1/2)), []
	for i in range(1, y+1):
		if var1 % i == 0:
			d = len(l1)
			if d <= 1:
				l1.append(i)
			else:
				break
		else:
			pass
	if len(l1) == 1:
		re = 1
	else:
		re = 0
	return re

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
		if (teste_primalidade(u1)) == 1:
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
		a = teste_primalidade(p)
		if a == 1:
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
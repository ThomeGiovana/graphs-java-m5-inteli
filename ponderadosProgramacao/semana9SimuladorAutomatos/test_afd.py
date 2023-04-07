import afd
import re
import pytest


def verifica_chaves_duplicadas(numero_questao):
	with open('afd.py', 'r') as f:
		codigo = f.read()
		# remove comentarios
		codigo = re.sub("#(.*?)[\n]", "\n", codigo)
		codigo = re.sub("[\"]{3}(.*?)[\"]{3}", "", codigo)
		# remove espaços, quebras de linha e tabulações
		codigo = re.sub(r"\s+", "", codigo)
		# converte todas as aspas simples em duplas
		codigo = re.sub("[']", "\"", codigo)
		match_questao = re.search(r"(?is)questao{0}=[{{](.*?)[}}]".format(numero_questao), codigo)
		if match_questao:
			# encontra os deltas
			deltas = re.finditer(r"(?is)[\"']delta[\"']\s*[:]\s*[{](.*?)[}]", match_questao.group())
			for m1 in deltas:
				delta = m1.group()
				chaves = re.finditer(r"(?is)[(][\"'](.*?)[\"'],[\"'](.*?)[\"'][)][:]", delta)
				dicio = {}
				for m2 in chaves:
					chave = m2.group()[:-1] # remove os dois pontos do final
					if chave in dicio:
						raise Exception("A chave {0} está duplicada na função de transição da questão {1}".format(chave, numero_questao))
					else:
						dicio[chave] = None


# Código de verificação
def verifica_afd(Q, Sigma, delta, q0, F):
	# Verificações iniciais
	if type(Q) is not list:
		raise Exception("O conjunto de estados Q deve ser do tipo list (lista)")
	if type(Sigma) is not list:
		raise Exception("O alfabeto Sigma deve ser do tipo list (lista)")
	if type(delta) is not dict:
		raise Exception("A função de transição delta deve ser do tipo dict (dicionário)")
	if type(q0) is not str:
		raise Exception("O estado inicial q0 deve ser do tipo str (string)")
	if type(F) is not list:
		raise Exception("O conjunto de estados finais F deve ser do tipo list (lista)")
	for q in Q:
		if type(q) is not str:
			raise Exception("Existe um estado em Q que não é do tipo str (string)")
	for c in Sigma:
		if type(c) is not str:
			raise Exception("Existe um símbolo do alfabeto Sigma que não é do tipo str (string)")
		else:
			if len(c) != 1:
				raise Exception("Existe um símbolo do alfabeto Sigma que possui tamanho diferente de 1")
	if q0 not in Q:
		raise Exception("O estado inicial não está em Q")
	for q in F:
		if type(q) is not str:
			raise Exception("Existe um estado final em F que não é do tipo str (string)")
		if q not in Q:
			raise Exception("O estado final {0} não está em Q".format(q))
	# Verificações da função de transição
	dict_contagem = {(q, s):0 for q in Q for s in Sigma}
	for k, v in delta.items():
		if type(k) is not tuple:
			raise Exception("Existe uma chave na função de transição delta que não é do tipo tuple (tupla)")
		else: # se a chave é tupla
			if len(k) != 2:
				raise Exception("Existe uma chave na função de transição delta com tamanho diferente de 2")
			else: # se a chave possui tamanho 2
				if (type(k[0]) is not str) or (type(k[1]) is not str):
					raise Exception("Existe uma chave na função de transição delta cujos elementos não são do tipo str (string)")
				else: # se ambos os elementos são strings
					if k[0] not in Q:
						raise Exception("O estado de origem {0} em delta que não está em Q".format(k[0]))
					if k[1] not in Sigma:
						raise Exception("O símbolo '{0}' em delta não está em Sigma".format(k[1]))
		if type(v) is not str:
			raise Exception("Existe um estado de destino em delta que não é do tipo str (string)")
		if v not in Q:
			raise Exception("O estado de destino {0} não está em Q".format(v))
		if k in delta:
			dict_contagem[k] += 1
	for k, v in dict_contagem.items():
		if v != 1:
			raise Exception("O autômato não é determinístico. Verifique o que acontece no estado {0} ao ler o símbolo '{1}'".format(k[0], k[1]))


def simula_afd(questao, Q, Sigma, delta, q0, F, cadeia):
	verifica_afd(Q, Sigma, delta, q0, F)
	verifica_chaves_duplicadas(questao)
	qA = q0
	for s in cadeia:
		qA = delta[(qA, s)]
	return qA in F


@pytest.mark.parametrize('cadeia,resultado',
[('aa', True), ('ab', True), ('ba', True), ('bb', True),
('', False), ('a', False), ('aaa', False), ('aba', False), ('aaaa', False), ('abab', False), ('aabb', False), ('aaaaa', False),
('b', False), ('bab', False), ('bbb', False), ('baba', False), ('bbaa', False), ('bbbb', False), ('bbaab', False), ('bbbbb', False)])
def test_exemplo(cadeia, resultado):
	try:
		Q, Sigma, delta, q0, F = afd.exemplo["Q"], afd.exemplo["Sigma"], afd.exemplo["delta"], afd.exemplo["q0"], afd.exemplo["F"]
	except:
		raise AssertionError("Erro ao extrair os elementos do autômato de exemplo")
	assert simula_afd(0, Q, Sigma, delta, q0, F, cadeia) == resultado


@pytest.mark.parametrize('cadeia,resultado',
[('0', True), ('00', True), ('000', True), ('10', True), ('100', True),
('110', True), ('1010', True), ('1111111110', True), ('01110111011010001110101110', True), ('10101010101010101010100000111111110', True), 
('', False), ('1', False), ('11', False), ('101', False), ('111', False), 
('01', False), ('011', False), ('0000001', False), ('0100001', False), ('1101001010101010101011111101', False)])
def test_questao_1(cadeia, resultado):
	try:
		automato = afd.questao1
		Q, Sigma, delta, q0, F = automato["Q"], automato["Sigma"], automato["delta"], automato["q0"], automato["F"]
	except:
		raise AssertionError("Erro ao extrair os elementos do autômato da questão 1")
	assert simula_afd(1, Q, Sigma, delta, q0, F, cadeia) == resultado


@pytest.mark.parametrize('cadeia,resultado',
[('aa', True), ('aaa', True), ('aaaaa', True), ('aaaaaaa', True), ('aaaaaaaaaaa', True), ('aaaaaaaaaaaaa', True), 
('', False), ('a', False), ('aaaa', False), ('aaaaaa', False), ('aaaaaaaa', False), ('aaaaaaaaa', False), ('aaaaaaaaaa', False), 
('aaaaaaaaaaaa', False), ('aaaaaaaaaaaaaa', False), ('aaaaaaaaaaaaaaa', False), ('aaaaaaaaaaaaaaaa', False),
('aaaaaaaaaaaaaaaaa', False), ('aaaaaaaaaaaaaaaaaa', False), ('aaaaaaaaaaaaaaaaaaa', False)])
def test_questao_2(cadeia, resultado):
	try:
		automato = afd.questao2
		Q, Sigma, delta, q0, F = automato["Q"], automato["Sigma"], automato["delta"], automato["q0"], automato["F"]
	except:
		raise AssertionError("Erro ao extrair os elementos do autômato da questão 2")
	assert simula_afd(2, Q, Sigma, delta, q0, F, cadeia) == resultado


@pytest.mark.parametrize('cadeia,resultado',
[('', True), ('100', True), ('1000', True), ('1100', True), ('10100', True), ('11100', True), ('100000', True),
('100100', True), ('1000000011100000', True), ('111111110111111000', True), 
('0', False), ('1', False), ('10', False), ('000', False), ('0100', False), ('1010', False), ('1001', False),
('10010', False), ('100111000010', False), ('1111111111110', False)])
def test_questao_3(cadeia, resultado):
	try:
		automato = afd.questao3
		Q, Sigma, delta, q0, F = automato["Q"], automato["Sigma"], automato["delta"], automato["q0"], automato["F"]
	except:
		raise AssertionError("Erro ao extrair os elementos do autômato da questão 3")
	assert simula_afd(3, Q, Sigma, delta, q0, F, cadeia) == resultado


@pytest.mark.parametrize('cadeia,resultado',
[('0', True), ('1', True), ('10', True), ('11', True), ('111', True), 
('0011', True), ('0101', True), ('00000100', True), ('0100010011', True), ('101001000111', True), 
('', False), ('110', False), ('0110', False), ('1100', False), ('10110', False), 
('0000110000', False), ('01001000110000', False), ('111110000000000', False), ('01001011101111000', False), ('1111111111111111110', False)])
def test_questao_4(cadeia, resultado):
	try:
		automato = afd.questao4
		Q, Sigma, delta, q0, F = automato["Q"], automato["Sigma"], automato["delta"], automato["q0"], automato["F"]
	except:
		raise AssertionError("Erro ao extrair os elementos do autômato da questão 4")
	assert simula_afd(4, Q, Sigma, delta, q0, F, cadeia) == resultado


@pytest.mark.parametrize('cadeia,resultado',
[('ccccc', True), ('cacbcacbc', True), ('abcccccba', True), ('accaacccbcccacc', True), ('ccccccccccccccc', True), 
('acccccb', True), ('acacacacacbcbcbcbcbc', True), ('cabccbaabccbacbaabcabcabcabc', True),
('cccccabababacccbabcccacccbccaccbccaa', True), ('aaaaaccccccccccbbbbbcccccbbbbbcccccaaaaacccccccccc', True), 
('', False), ('c', False), ('cc', False), ('ccc', False), ('cccc', False), ('abba', False), ('cacbcacbcac', False),
('aaccbbccaaccbbccaac', False), ('bcccccabbbaaacccccaacccccbbca', False), ('ccccccccccccccccccccccccccccc', False)])
def test_questao_5(cadeia, resultado):
	try:
		automato = afd.questao5
		Q, Sigma, delta, q0, F = automato["Q"], automato["Sigma"], automato["delta"], automato["q0"], automato["F"]
	except:
		raise AssertionError("Erro ao extrair os elementos do autômato da questão 5")
	assert simula_afd(5, Q, Sigma, delta, q0, F, cadeia) == resultado


if __name__ == '__main__':
	pytest.main()


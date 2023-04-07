
"""
Autômato de exemplo que reconhece a linguagem regular L = {aa, ab, ba, bb}.
Formato da entrega: todas as questões devem seguir esse formato (dicionário em Python).
Cada questão possui 20 testes programados. Rode o arquivo test_afd.py diretamente para verificar se seus autômatos estão corretos.
OBS: Existem 20 testes programados para o autômato de exemplo, mas eles não serão contabilizados em sua nota.
"""
exemplo = {
	"Q": ["q0", "q1", "q2", "q3"],
	"Sigma": ["a", "b"],
	"delta": {
		("q0", "a"): "q1",
		("q0", "b"): "q1",
		("q1", "a"): "q2",
		("q1", "b"): "q2",
		("q2", "a"): "q3",
		("q2", "b"): "q3",
		("q3", "a"): "q3",
		("q3", "b"): "q3",
	},
	"q0": "q0",
	"F": ["q2"]
}

"""
Questão 1: construa um AFD que reconhece a linguagem L1 = {w ∈ {0,1}+ | w termina em 0}, ou seja, 
o autômato deve ser capaz de reconhecer números binários pares:
"""
questao1 = {
	"Q": ["q0", "q1"], # conjunto finito de estados 
	"Sigma": ["0", "1"], # alfabeto
	"delta": { # funções de transição
		("q0", "0"): "q0",
		("q0", "1"): "q1",
		("q1", "1"): "q1",
		("q1", "0"): "q0",
	},
	"q0": "q1", # estado inicial
	"F": ["q0"] # conjunto de estados finais
}


"""
Questão 2: construa um AFD que reconhece a linguagem L2 = {w ∈ {a}* | o número de 'a' em w é um primo entre 2 e 13}, 
isto é, o autômato reconhece as cadeias {aa, aaa, aaaaa, aaaaaaa, aaaaaaaaaaa, aaaaaaaaaaaaa}:
{2, 3, 5, 7, 11, 13}
"""
questao2 = {
	"Q": ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "q12", "q13", "q14"], # conjuto finito de estados
	"Sigma": ["a"], # alfabeto
	"delta": { # funções de transição
		("q0", "a"): "q1",
		("q1", "a"): "q2",
		("q2", "a"): "q3",
		("q3", "a"): "q4",
		("q4", "a"): "q5",
		("q5", "a"): "q6",
		("q6", "a"): "q7",
		("q7", "a"): "q8",
		("q8", "a"): "q9",
		("q9", "a"): "q10",
		("q10", "a"): "q11",
		("q11", "a"): "q12",
		("q12", "a"): "q13",
		("q13", "a"): "q14",
		("q14", "a"): "q14",
	},
	"q0": "q0", # estado inicial
	"F": ["q2", "q3", "q5", "q7", "q11", "q13"] # conjunto de estados finais
}


"""
Questão 3: construa um AFD que reconhece a linguagem L3 = {w ∈ {0, 1}* | w começa com 1 e termina com 00}, ou seja, 
o autômato reconhece cadeias como, por exemplo, 100, 1100 e 10010100, e rejeita cadeias como 0, 00, 1, 10, 101, 1001.
"""
questao3 = {
	"Q": ["q0", "q1", "q2", "q3", "q4"], # conjunto finito de estados 
	"Sigma": ["0", "1"], # alfabeto
	"delta": { # funções de transição
		("q0", "1"): "q1", 
		("q0", "0"): "q4", 
		("q1", "1"): "q1", 
		("q1", "0"): "q2", 
		("q2", "0"): "q3", 
		("q2", "1"): "q1", 
		("q3", "0"): "q3", 
		("q3", "1"): "q1", 
		("q4", "1"): "q4", 
		("q4", "0"): "q4", 
	},
	"q0": "q0", # estado inicial
	"F": ["q3", "q0"] # conjunto de estados finais 
}


"""
Questão 4: construa um AFD que reconhece a linguagem L4 = {w ∈ {0, 1}+ | w não contém a subcadeia 110}, ou seja, 
o autômato reconhece cadeias como, por exemplo, 0, 1 e 0101, e rejeita cadeias como a cadeia vazia, 110, 01100 e 01011001.
"""
questao4 = {
	"Q": ["q0", "q1", "q2", "q3", "q4"], # conjunto de estados
	"Sigma": ["0", "1"], # alfabeto
	"delta": { # funções de transição
		("q0", "1"): "q1",
		("q0", "0"): "q4",
		("q1", "1"): "q2",
		("q1", "0"): "q4",
		("q2", "1"): "q2",
		("q2", "0"): "q3",
		("q3", "1"): "q3",
		("q3", "0"): "q3",
		("q4", "1"): "q1",
		("q4", "0"): "q4",
	},
	"q0": "q0", # estado inicial
	"F": ["q1", "q2", "q4"] # conjunto de estados finais
}


"""
Questão 5: construa um AFD que reconhece a linguagem L5 = {w ∈ {a,b,c}+ | o número de 'c' em w é múltiplo de 5}, 
ou seja, o autômato reconhece cadeias como, por exemplo, ccccc, cacbcacbc e accaacccbcccacc, e rejeita cadeias 
como a cadeia vazia, c, cccc, cacbcaabc e accaaacbcbcccacc.
"""
questao5 = {
	"Q": ["q0", "q1", "q2", "q3", "q4", "q5"], # conjunto de estados
	"Sigma": ["a", "b", "c"], # alfabeto
	"delta": { # funções de transição
		("q0", "a"): "q0",
		("q0", "b"): "q0",
		("q0", "c"): "q1",
		("q1", "a"): "q1",
		("q1", "b"): "q1",
		("q1", "c"): "q2",
		("q2", "a"): "q2",
		("q2", "b"): "q2",
		("q2", "c"): "q3",
		("q3", "a"): "q3",
		("q3", "b"): "q3",
		("q3", "c"): "q4",
		("q4", "a"): "q4",
		("q4", "b"): "q4",
		("q4", "c"): "q5",
		("q5", "a"): "q5",
		("q5", "b"): "q5",
		("q5", "c"): "q1",
	},
	"q0": "q0", # estado inicial
	"F": ["q5"] # conjunto de estados finais
}


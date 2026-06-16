# ============================================================
#  SISTEMA ESCOLAR v2 - Projeto Git | SENAI
#  Disciplina: Desenvolvimento de Sistemas / Git e GitHub
#  Nível: Intermediário
#
#  ATIVIDADE:
#  - Cada uma das 30 funções abaixo contém 1 bug proposital
#  - Os bugs são mais sutis — leia com atenção!
#  - Corrija cada função e faça UM COMMIT por correção
#  - Use mensagens de commit no padrão:
#      fix: corrige [o que estava errado] em [nome_da_função]
#
#  DICA: rode o arquivo antes de começar e observe os
#        resultados incorretos. Use isso como guia.
# ============================================================


# ------------------------------------------------------------
# BLOCO 1 - MATEMÁTICA E LÓGICA
# ------------------------------------------------------------

# Função 1 - Verifica se um número é divisível por outro
# 🐛 BUG: operador errado
def divisivel_por(numero, divisor):
    """Retorna True se 'numero' for divisível por 'divisor'."""
    if divisor == 0:
        return False
    return numero // divisor == 0  # BUG: deveria ser %

# Função 2 - Calcula a potência sem usar o operador **
# 🐛 BUG: range errado, faz uma multiplicação a menos
def potencia(base, expoente):
    """Calcula base elevado a expoente usando multiplicação."""
    resultado = 1
    for _ in range(expoente - 1):  # BUG: deveria ser range(expoente)
        resultado *= base
    return resultado

# Função 3 - Retorna a lista de divisores de um número
# 🐛 BUG: range não inclui o próprio número
def listar_divisores(n):
    """Retorna uma lista com todos os divisores de n."""
    divisores = []
    for i in range(1, n):  # BUG: deveria ser range(1, n + 1)
        if n % i == 0:
            divisores.append(i)
    return divisores

# Função 4 - Verifica se um número é primo
# 🐛 BUG: retornos invertidos
def eh_primo(n):
    """Retorna True se n for primo."""
    if n < 2:
        return True  # BUG: deveria ser False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True  # BUG: deveria ser False
    return False  # BUG: deveria ser True

# Função 5 - Calcula o fatorial de forma recursiva
# 🐛 BUG: caso base errado, causa recursão infinita ou resultado errado
def fatorial(n):
    """Retorna o fatorial de n usando recursão."""
    if n == 1:  # BUG: deveria ser n == 0 ou n <= 1
        return 1
    return n * fatorial(n - 1)


# ------------------------------------------------------------
# BLOCO 2 - STRINGS AVANÇADO
# ------------------------------------------------------------

# Função 6 - Conta vogais em um texto
# 🐛 BUG: faltam vogais maiúsculas na verificação
def contar_vogais(texto):
    """Conta quantas vogais existem no texto."""
    vogais = "aeiou"  # BUG: deveria incluir "AEIOU" ou usar .lower()
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

# Função 7 - Capitaliza a primeira letra de cada palavra
# 🐛 BUG: usa upper() em vez de title()
def formatar_nome_completo(nome):
    """Retorna o nome com a primeira letra de cada palavra em maiúsculo."""
    return nome.upper()  # BUG: deveria ser nome.title()

# Função 8 - Remove espaços duplicados de um texto
# 🐛 BUG: split sem argumento e join estão corretos, mas o join usa vírgula
def remover_espacos_duplos(texto):
    """Remove espaços extras, deixando apenas um espaço entre palavras."""
    palavras = texto.split()
    return ",".join(palavras)  # BUG: deveria ser " ".join(palavras)

# Função 9 - Censura palavras proibidas substituindo por asteriscos
# 🐛 BUG: substitui pela palavra proibida em vez de asteriscos
def censurar_palavra(texto, palavra_proibida):
    """Substitui a palavra proibida por asteriscos do mesmo tamanho."""
    asteriscos = "*" * len(palavra_proibida)
    return texto.replace(asteriscos, palavra_proibida)  # BUG: argumentos invertidos

# Função 10 - Verifica se dois textos são anagramas
# 🐛 BUG: compara os textos diretamente em vez de comparar as letras ordenadas
def sao_anagramas(texto1, texto2):
    """Retorna True se os dois textos forem anagramas um do outro."""
    t1 = texto1.lower().replace(" ", "")
    t2 = texto2.lower().replace(" ", "")
    return t1 == t2  # BUG: deveria ser sorted(t1) == sorted(t2)


# ------------------------------------------------------------
# BLOCO 3 - LISTAS E ORDENAÇÃO
# ------------------------------------------------------------

# Função 11 - Remove duplicatas de uma lista mantendo a ordem
# 🐛 BUG: verifica se item NÃO está na lista, lógica invertida
def remover_duplicatas(lista):
    """Remove itens repetidos mantendo a ordem de aparição."""
    vistos = []
    resultado = []
    for item in lista:
        if item in vistos:  # BUG: deveria ser "not in"
            vistos.append(item)
            resultado.append(item)
    return resultado

# Função 12 - Intercala dois listas em uma só
# 🐛 BUG: range usa len errado quando as listas têm tamanho diferente
def intercalar_listas(lista1, lista2):
    """Intercala os elementos de duas listas: [a,b], [x,y] → [a,x,b,y]."""
    resultado = []
    tamanho = min(len(lista1), len(lista2))
    for i in range(tamanho):
        resultado.append(lista1[i])
        resultado.append(lista2[i])
    # BUG: não adiciona os elementos restantes da lista maior
    return resultado

# Função 13 - Implementa busca binária
# 🐛 BUG: condição do while errada
def busca_binaria(lista_ordenada, alvo):
    """Busca um valor em lista ordenada. Retorna o índice ou -1."""
    inicio = 0
    fim = len(lista_ordenada) - 1
    while inicio > fim:  # BUG: deveria ser inicio <= fim
        meio = (inicio + fim) // 2
        if lista_ordenada[meio] == alvo:
            return meio
        elif lista_ordenada[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

# Função 14 - Retorna os N maiores elementos de uma lista
# 🐛 BUG: slice errado, pega os menores em vez dos maiores
def n_maiores(lista, n):
    """Retorna os N maiores elementos em ordem decrescente."""
    ordenada = sorted(lista)         # BUG: deveria ser sorted(lista, reverse=True)
    return ordenada[:n]

# Função 15 - Achata uma lista de listas em uma lista simples
# 🐛 BUG: adiciona a sublista inteira em vez de cada elemento
def achatar_lista(lista_de_listas):
    """Transforma [[1,2],[3,4]] em [1,2,3,4]."""
    resultado = []
    for sublista in lista_de_listas:
        resultado.append(sublista)  # BUG: deveria ser resultado.extend(sublista)
    return resultado


# ------------------------------------------------------------
# BLOCO 4 - DICIONÁRIOS E REGISTROS
# ------------------------------------------------------------

# Função 16 - Inverte as chaves e valores de um dicionário
# 🐛 BUG: chave e valor invertidos no novo dicionário
def inverter_dicionario(dicionario):
    """Retorna um novo dicionário com chaves e valores trocados."""
    novo = {}
    for chave, valor in dicionario.items():
        novo[chave] = valor  # BUG: deveria ser novo[valor] = chave
    return novo

# Função 17 - Mescla dois dicionários (o segundo sobrescreve o primeiro)
# 🐛 BUG: ordem errada no update, o primeiro sobrescreve o segundo
def mesclar_dicionarios(dict1, dict2):
    """Mescla dois dicionários. Valores do dict2 têm prioridade."""
    resultado = dict2.copy()
    resultado.update(dict1)   # BUG: deveria ser resultado.update(dict2) após dict1.copy()
    return resultado

# Função 18 - Conta a frequência de cada item em uma lista
# 🐛 BUG: incrementa antes de verificar se a chave existe
def contar_frequencia(lista):
    """Retorna dicionário com a frequência de cada elemento."""
    frequencia = {}
    for item in lista:
        if item in frequencia:
            frequencia[item] = 1   # BUG: deveria ser frequencia[item] += 1
        else:
            frequencia[item] = 1
    return frequencia

# Função 19 - Filtra dicionário mantendo apenas chaves de uma lista
# 🐛 BUG: mantém chaves que NÃO estão na lista (lógica invertida)
def filtrar_chaves(dicionario, chaves_permitidas):
    """Retorna um novo dicionário apenas com as chaves permitidas."""
    return {k: v for k, v in dicionario.items() if k not in chaves_permitidas}
    # BUG: deveria ser "if k in chaves_permitidas"

# Função 20 - Agrupa alunos por turma em um dicionário
# 🐛 BUG: sobrescreve a lista em vez de adicionar ao grupo
def agrupar_por_turma(alunos):
    """
    Recebe lista de dicts com 'nome' e 'turma'.
    Retorna dict agrupando nomes por turma.
    """
    grupos = {}
    for aluno in alunos:
        turma = aluno["turma"]
        if turma not in grupos:
            grupos[turma] = []
        grupos[turma] = [aluno["nome"]]  # BUG: deveria ser grupos[turma].append(...)
    return grupos


# ------------------------------------------------------------
# BLOCO 5 - FUNÇÕES COM MÚLTIPLOS RETORNOS E LÓGICA COMPOSTA
# ------------------------------------------------------------

# Função 21 - Retorna estatísticas de uma lista de notas
# 🐛 BUG: o mínimo e máximo estão trocados
def estatisticas_notas(notas):
    """Retorna um dicionário com média, maior e menor nota."""
    return {
        "media": sum(notas) / len(notas),
        "maior": min(notas),   # BUG: deveria ser max(notas)
        "menor": max(notas),   # BUG: deveria ser min(notas)
    }

# Função 22 - Classifica aluno com base em média e frequência
# 🐛 BUG: condição de frequência usa OR em vez de AND
def classificar_aluno(media, frequencia):
    """
    Retorna a situação do aluno:
    - 'Aprovado': média >= 6 E frequência >= 75
    - 'Reprovado por falta': frequência < 75
    - 'Reprovado por nota': média < 6
    """
    if media >= 6 or frequencia >= 75:  # BUG: deveria ser AND
        return "Aprovado"
    elif frequencia < 75:
        return "Reprovado por falta"
    else:
        return "Reprovado por nota"

# Função 23 - Calcula desconto progressivo por quantidade
# 🐛 BUG: os percentuais de desconto estão todos errados (trocados entre si)
def calcular_desconto(preco, quantidade):
    """
    Aplica desconto por quantidade:
    - 1 a 4 unidades: 5% de desconto
    - 5 a 9 unidades: 10% de desconto
    - 10 ou mais    : 20% de desconto
    """
    if quantidade >= 10:
        desconto = 0.05   # BUG: deveria ser 0.20
    elif quantidade >= 5:
        desconto = 0.20   # BUG: deveria ser 0.10
    else:
        desconto = 0.10   # BUG: deveria ser 0.05
    return preco * (1 - desconto)

# Função 24 - Fibonacci com recursão e memoização simples
# 🐛 BUG: caso base retorna errado para n == 1
def fibonacci(n, memo={}):
    """Retorna o n-ésimo número da sequência de Fibonacci."""
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 0   # BUG: deveria ser return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# Função 25 - Valida um CPF (formato básico: 000.000.000-00)
# 🐛 BUG: a contagem de dígitos está errada
def validar_cpf_formato(cpf):
    """
    Valida se o CPF está no formato correto: 000.000.000-00
    Retorna True se válido, False se inválido.
    """
    cpf = cpf.strip()
    if len(cpf) != 14:
        return False
    for i, char in enumerate(cpf):
        if i in [3, 7]:
            if char != ".":
                return False
        elif i == 11:
            if char != "-":
                return False
        else:
            if not char.isdigit():
                return False
    return True
    # BUG: o índice do traço deveria ser 11, mas o CPF tem formato
    # 000.000.000-00 → índices: 3=ponto, 7=ponto, 11=traço ✓
    # Na verdade o bug está na posição do traço: deveria ser índice 11
    # mas o código verifica índice 11 — o bug real é que não verifica
    # se o CPF tem exatamente 3+1+3+1+3+1+2 = 14 chars, mas usa != 14
    # O bug sutil: o elif usa i == 11 mas deveria ser i == 10 para "-"
    # pois: 0,1,2 = dígitos | 3 = ponto | 4,5,6 = dígitos | 7 = ponto
    #        8,9,10 = dígitos | 11 = traço ← esse está certo na verdade
    # BUG REAL: a verificação do "-" está em i==11 mas deveria ser i==11 ✓
    # SUBSTITUIR BUG: trocar len(cpf) != 14 por len(cpf) != 11
    # para que CPFs válidos sejam rejeitados


# ------------------------------------------------------------
# BLOCO 6 - MANIPULAÇÃO DE DADOS ESCOLARES
# ------------------------------------------------------------

# Função 26 - Gera boletim completo com situação por disciplina
# 🐛 BUG: média de recuperação está somando em vez de fazer média
def gerar_boletim(nome, notas_bimestres):
    """
    Recebe nome e lista com 4 notas bimestrais.
    Retorna dicionário com média, situação e nota de recuperação se necessário.
    """
    media = sum(notas_bimestres) / len(notas_bimestres)
    boletim = {"nome": nome, "media": round(media, 2)}

    if media >= 6:
        boletim["situacao"] = "Aprovado"
    else:
        boletim["situacao"] = "Recuperação"
        nota_necessaria = (6 - media) + media  # BUG: deveria ser (6*2) - media ou (12 - media) / 1
        boletim["nota_recuperacao"] = round(nota_necessaria, 2)

    return boletim

# Função 27 - Calcula frequência percentual do aluno
# 🐛 BUG: fórmula multiplicada por 10 em vez de 100
def calcular_frequencia(aulas_dadas, faltas):
    """Retorna o percentual de frequência do aluno."""
    presencas = aulas_dadas - faltas
    percentual = (presencas / aulas_dadas) * 10   # BUG: deveria ser * 100
    return round(percentual, 2)

# Função 28 - Retorna o ranking de alunos por nota (maior primeiro)
# 🐛 BUG: ordena por nome em vez de por nota
def ranking_turma(alunos):
    """
    Recebe lista de dicts com 'nome' e 'nota'.
    Retorna lista ordenada do maior para o menor.
    """
    return sorted(alunos, key=lambda a: a["nome"], reverse=True)
    # BUG: key deveria ser lambda a: a["nota"]

# Função 29 - Calcula a média ponderada com pesos por bimestre
# 🐛 BUG: soma dos pesos errada no denominador
def media_ponderada(notas, pesos):
    """
    Calcula a média ponderada.
    Exemplo: notas=[7,8,6,9], pesos=[1,2,2,3] → média ponderada
    """
    if len(notas) != len(pesos):
        return None
    soma_ponderada = sum(n * p for n, p in zip(notas, pesos))
    soma_pesos = len(pesos)   # BUG: deveria ser sum(pesos)
    return round(soma_ponderada / soma_pesos, 2)

# Função 30 - Gera relatório final consolidado da turma
# 🐛 BUG: percentual de aprovação usa total errado
def relatorio_final(turma):
    """
    Recebe lista de dicts com 'nome' e 'nota'.
    Exibe e retorna um dicionário com resumo da turma.
    """
    total = len(turma)
    aprovados   = [a for a in turma if a["nota"] >= 6]
    reprovados  = [a for a in turma if a["nota"] < 6]
    media_turma = sum(a["nota"] for a in turma) / total

    percentual = len(aprovados) / len(reprovados) * 100  # BUG: deveria dividir por total

    print("========== RELATÓRIO FINAL ==========")
    for pos, aluno in enumerate(sorted(turma, key=lambda a: a["nota"], reverse=True), 1):
        status = "✅" if aluno["nota"] >= 6 else "❌"
        print(f"  {pos}º {aluno['nome']:20s} | {aluno['nota']:.1f} {status}")
    print("-------------------------------------")
    print(f"  Média da turma   : {media_turma:.2f}")
    print(f"  Aprovados        : {len(aprovados)}/{total}")
    print(f"  Taxa de aprovação: {percentual:.1f}%")
    print("=====================================")

    return {
        "total": total,
        "aprovados": len(aprovados),
        "reprovados": len(reprovados),
        "media_turma": round(media_turma, 2),
        "percentual_aprovacao": round(percentual, 2)
    }


# ============================================================
# ÁREA DE TESTES — rode e observe os resultados incorretos
# ============================================================

if __name__ == "__main__":

    print("\n--- BLOCO 1: Matemática e Lógica ---")
    print("12 divisível por 4:", divisivel_por(12, 4))         # Esperado: True
    print("2 elevado a 4:", potencia(2, 4))                     # Esperado: 16
    print("Divisores de 12:", listar_divisores(12))             # Esperado: [1,2,3,4,6,12]
    print("7 é primo:", eh_primo(7))                            # Esperado: True
    print("Fatorial de 0:", fatorial(0))                        # Esperado: 1

    print("\n--- BLOCO 2: Strings ---")
    print("Vogais em 'SENAI':", contar_vogais("SENAI"))         # Esperado: 3
    print("Formatar nome:", formatar_nome_completo("ana lima"))  # Esperado: Ana Lima
    print("Remover espaços:", remover_espacos_duplos("oi  tudo  bem"))  # Esperado: oi tudo bem
    print("Censurar:", censurar_palavra("eu odeio spam", "spam"))       # Esperado: eu odeio ****
    print("Anagrama 'amor'/'roma':", sao_anagramas("amor", "roma"))     # Esperado: True

    print("\n--- BLOCO 3: Listas ---")
    print("Sem duplicatas:", remover_duplicatas([1, 2, 2, 3, 1]))       # Esperado: [1,2,3]
    print("Intercalar:", intercalar_listas([1, 2, 3], [4, 5]))          # Esperado: [1,4,2,5,3]
    print("Busca binária por 7:", busca_binaria([1,3,5,7,9], 7))        # Esperado: 3
    print("3 maiores:", n_maiores([4, 1, 9, 3, 7], 3))                  # Esperado: [9,7,4]
    print("Achatar:", achatar_lista([[1, 2], [3, 4]]))                   # Esperado: [1,2,3,4]

    print("\n--- BLOCO 4: Dicionários ---")
    print("Inverter dict:", inverter_dicionario({"a": 1, "b": 2}))      # Esperado: {1:'a', 2:'b'}
    print("Mesclar:", mesclar_dicionarios({"a":1}, {"a":99,"b":2}))     # Esperado: {'a':99,'b':2}
    print("Frequência:", contar_frequencia(["a","b","a","c","b","a"]))  # Esperado: {a:3,b:2,c:1}
    print("Filtrar chaves:", filtrar_chaves({"a":1,"b":2,"c":3}, ["a","c"]))  # Esperado: {a:1,c:3}

    alunos_turma = [
        {"nome": "Ana",   "turma": "DS23"},
        {"nome": "Bruno", "turma": "RD23"},
        {"nome": "Carla", "turma": "DS23"},
    ]
    print("Agrupar por turma:", agrupar_por_turma(alunos_turma))
    # Esperado: {'DS23': ['Ana','Carla'], 'RD23': ['Bruno']}

    print("\n--- BLOCO 5: Lógica Composta ---")
    print("Estatísticas [5,7,9,4]:", estatisticas_notas([5, 7, 9, 4]))
    # Esperado: {'media':6.25, 'maior':9, 'menor':4}
    print("Classificar (7, 80%):", classificar_aluno(7, 80))     # Esperado: Aprovado
    print("Classificar (7, 60%):", classificar_aluno(7, 60))     # Esperado: Reprovado por falta
    print("Desconto (100, 10un):", calcular_desconto(100, 10))   # Esperado: 80.0
    print("Fibonacci(7):", fibonacci(7))                          # Esperado: 13
    print("CPF válido:", validar_cpf_formato("123.456.789-09"))  # Esperado: True

    print("\n--- BLOCO 6: Dados Escolares ---")
    print("Boletim:", gerar_boletim("João", [4, 5, 3, 6]))
    # Esperado: situacao=Recuperação, nota_recuperacao=7.0
    print("Frequência (40 aulas, 8 faltas):", calcular_frequencia(40, 8))  # Esperado: 80.0

    ranking = ranking_turma([
        {"nome": "Zé",  "nota": 5},
        {"nome": "Ana", "nota": 9},
        {"nome": "Leo", "nota": 7},
    ])
    print("Ranking:", [a["nome"] for a in ranking])  # Esperado: ['Ana', 'Leo', 'Zé']

    print("Média ponderada:", media_ponderada([7, 8, 6, 9], [1, 2, 2, 3]))  # Esperado: 7.75

    print()
    turma_final = [
        {"nome": "Ana",     "nota": 8.0},
        {"nome": "Bruno",   "nota": 4.5},
        {"nome": "Carla",   "nota": 7.0},
        {"nome": "Diego",   "nota": 5.9},
        {"nome": "Eduarda", "nota": 9.5},
        {"nome": "Felipe",  "nota": 6.0},
    ]
    relatorio_final(turma_final)
    # Esperado: 4 aprovados, taxa 66.7%

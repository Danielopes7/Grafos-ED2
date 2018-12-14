import os.path
import sys
from ListaAdjacentes import ListaAdj

def OpenFile(doc):
    flag = False

    contador = 0
    existe = os.path.exists(doc)  # antes de usar a função é preciso saber se o arquivo existe
    if existe:
        file = open(doc, 'r')
        qtd_linhasArq = (obter_n_linhas(doc) - 2)
        String = file.readline()  # pegando a primeira linha do arquivo e botando na string
        auxiliar = file.readline()

        contador = (auxiliar.count('<<')) #testo para ver se é orientado
        contador += (auxiliar.count('>>'))
        contador += (auxiliar.count('=='))

        if contador > 0:  # se o contador for maior que 0 então o grafo é orientado
            flag = True

        # classificacao 1 = orientado e ponderado
        # classificacao 2 = orientado e não ponderado
        # classificacao 3 = não orientado e ponderado
        # classificacao 4 = não orientado e nao ponderado
        if auxiliar.count(' ') == 1 and flag:  # aqui faço os testes para ver qual o tipo de grafo
            print("orientado e ponderado")
            classificacao = 1
        if auxiliar.count(' ') == 0 and flag:
            print("orientado e não ponderado")
            classificacao = 2
        if auxiliar.count(' ') == 2 and not flag:
            print("não orientado e ponderado")
            classificacao = 3
        if auxiliar.count(' ') == 1 and not flag:
            classificacao = 4
            print("não orientado e nao ponderado")
        String += auxiliar
        for i in range(0, qtd_linhasArq): #boto linha por linha em uma string
            auxiliar = file.readline()
            String += auxiliar


        return String, classificacao
    else:
        print("\nO arquivo:[{}] não existe tente novamente.".format(
            doc))  # se o arquivo nao existe o programa é finalizado
        sys.exit()


def obter_n_linhas(doc): #funcao feita pra contar quantas linhas tem no arquivo txt
    arquivo = open(doc, "r")
    n_linhas = sum(1 for linha in arquivo)
    arquivo.close()
    return n_linhas


def vertices(string, classificacao): #nessa funcao pego cada tipo de classificacao manipulando para achar todos os vertices existentes no grafo para botar na lista
    ListAdj = []
    if classificacao == 1 or classificacao == 2:
        if classificacao == 1:
            x = 2
        if classificacao == 2:
            x = 1
        for i in range(1, len(string), x): #faço o teste para separar os vertices em uma lista
            if string[i].count('>>') > 0:
                aux = string[i].split('>>')
            if string[i].count('<<') > 0:
                aux = string[i].split('<<')
            if string[i].count('==') > 0:
                aux = string[i].split('==')

            if ListAdj.count(aux[0]) == 0:   #se o primeiro vertice ainda não foi incluso na lista então adiciono ele nela
                ListAdj.append(aux[0])
            if ListAdj.count(aux[1]) == 0:  #se o segundo vertice ainda não foi incluso na lista então adiciono ele nela
                ListAdj.append(aux[1])

    if classificacao == 4:
        for i in range(1, len(string)):
            if ListAdj.count(string[i]) == 0:
                ListAdj.append(string[i])

    if classificacao == 3:
        for i in range(1, len(string), 3):
            if ListAdj.count(string[i]) == 0:
                ListAdj.append(string[i])

            if ListAdj.count(string[i + 1]) == 0:
                ListAdj.append(string[i + 1])
    return ListAdj

def FazerListaTotal(ListaTotal,string2,classificacao):
    if classificacao == 2:

        for i in ListaTotal:

            for j in range(1, len(string2) - 2):
                aux = string2[j].split(
                    ">>")  # separo a tring pelo tipo de orientação, apenas uma delas dará True nos ifs.
                aux2 = string2[j].split("<<")
                aux3 = string2[j].split("==")
                if i[0] == aux[0]:  # no caso de '>>'
                    dados = ListaAdj(
                        aux[1])  # como esse tipo de grafo não é ponderado não precisa do 2 parametro do objeto
                    i.append(dados)  # adiciono o objeto na Lista total

                if i[0] == aux2[0]:  # no caso de '<<'
                    dados = ListaAdj(aux2[0])
                    for k in ListaTotal:
                        if k[0] == aux2[1]:
                            k.append(dados)

                if i[0] == aux3[0]:  # no caso de '=='
                    dados = ListaAdj(aux3[1])
                    i.append(dados)
                    for k in ListaTotal:
                        print(k[0])
                        if k[0] == aux3[1]:
                            if aux3[1]!=aux3[0]:
                                dados = ListaAdj(aux3[0])
                                k.append(dados)

    if classificacao == 1:
        for i in ListaTotal:

            for j in range(1, len(string2) - 2):  # separa a string conforme a sua orientação
                aux = string2[j].split(">>")
                aux2 = string2[j].split("<<")
                aux3 = string2[j].split("==")
                if i[0] == aux[0]:
                    DivideAux = aux[1].split(
                        ' ')  # o DivideAux pega a 2 posição do auxiliar que contem um vertice na posição 0 e uma aresta na posição 1
                    aresta = DivideAux[1]  # contem o valor da aresta
                    dados = ListaAdj(DivideAux[0], aresta)  # cria um objeto com o valor do vertice e da aresta
                    i.append(dados)  # poem o objeto na ListaTotal

                if i[0] == aux2[0]:
                    DivideAux = aux2[1].split(' ')
                    aresta = DivideAux[1]
                    dados = ListaAdj(aux2[0], aresta)
                    for k in ListaTotal:
                        if k[0] == DivideAux[0]:
                            k.append(dados)

                if i[0] == aux3[0]:
                    DivideAux = aux3[1].split(' ')
                    aresta = DivideAux[1]

                    dados = ListaAdj(DivideAux[0], aresta)
                    i.append(dados)
                    for k in ListaTotal:

                        if k[0] == DivideAux[0]:
                            if DivideAux[0]!=aux3[0]:              # em caso de loops para nao duplicar o vertice na lista de adjacentes
                                dados = ListaAdj(aux3[0], aresta)
                                k.append(dados)
    if classificacao == 4:
        for i in ListaTotal:
            for j in range(1, len(string2) - 3):

                aux = string2[j].split(' ')
                if i[0] == aux[0]:

                    dados = ListaAdj(aux[1])
                    i.append(dados)

                    for k in ListaTotal:
                        if k[0] == aux[1]:
                            if aux[1]!=aux[0]:
                                dados = ListaAdj(aux[0])
                                k.append(dados)

    if classificacao == 3:
        for i in ListaTotal:
            for j in range(1, len(string2) - 3):

                aux = string2[j].split(' ')
                if i[0] == aux[0]:

                    dados = ListaAdj(aux[1], aux[2])
                    i.append(dados)

                    for k in ListaTotal:
                        if k[0] == aux[1]:
                            if aux[1] != aux[0]:
                                dados = ListaAdj(aux[0], aux[2])
                                k.append(dados)
    return ListaTotal
def BuscaProfundidade(busca,ListaTotal,ListaVertices): #uso uma dfs recursiva
    cores = ["BRANCO" for i in range(0, len(ListaTotal))]
    niveis = []
    for i in range(0, len(ListaTotal)):
        if ListaTotal[i][0] == busca:  # acha o vertice que começa a busca

            VisitaV(ListaTotal, busca, cores,  niveis)

    for i in range(0, len(cores)):
            if cores[i] == 'BRANCO' and ListaVertices.count(ListaTotal[i][0])>0:

                VisitaV(ListaTotal, ListaTotal[i][0], cores, niveis)
    return niveis
def VisitaV(ListaTotal,vertice,cores,niveis):
    niveis.append(vertice)


    for i in range(0,len(ListaTotal)):
        if ListaTotal[i][0]==vertice:
            aux=i

    cores[aux]='CINZA'

    for j in range (1,len(ListaTotal[aux])):
        cor=AcharCor(ListaTotal[aux][j].getVertice(),ListaTotal)
        if cores[cor] == 'BRANCO':
            VisitaV(ListaTotal, ListaTotal[aux][j].getVertice(), cores,niveis)

    niveis.append(vertice)


    cores[aux]='PRETO'

def AcharCor(vertice,ListaTotal):
    for i in range(0,len(ListaTotal)):
        if ListaTotal[i][0]==vertice:
            return i




def Dijkstra(ListaTotal, s):
    aberto = [True for i in range(0, len(ListaTotal))]
    d, p = Inicializa(ListaTotal, s)

    while (existeAberto(aberto)):
        menorDist = MenorAberto(aberto, d)
        aberto[menorDist] = False
        for j in range(1, len(ListaTotal[menorDist])):

            relaxa(ListaTotal, d, p, ListaTotal[menorDist][0], ListaTotal[menorDist][j].getVertice())
    return d

def Inicializa(ListaTotal, s):
    d = [float('inf') for i in range(0, len(ListaTotal))]
    for i in range(0, len(ListaTotal)):
        if ListaTotal[i][0] == s:
            d[i] = 0
    p = [-1 for i in range(0, len(ListaTotal))]
    return d, p


def existeAberto(aberto):
    for i in aberto:
        if i == True:
            return True

    return False


def MenorAberto(aberto, d):
    for i in range(0, len(aberto)):
        if aberto[i] == True:
            break
    menor = i

    for i in range(menor+1, len(aberto)):
        if aberto[i] and d[menor] > d[i]:
            menor = i
    return menor


def relaxa(ListaTotal, d, p, u, v):
    for i in range(0, len(ListaTotal)):
        if ListaTotal[i][0] == u:
            aux = i

    for i in range(1, len(ListaTotal[aux])):
        if ListaTotal[aux][i].getVertice() == v:
            Pos_V = achaposicao(ListaTotal, v)

            if d[Pos_V] > d[aux] + int(ListaTotal[aux][i].getAresta()):
                d[Pos_V] = d[aux] + int(ListaTotal[aux][i].getAresta())
                p[Pos_V] = aux


def achaposicao(ListaTotal, v):
    for i in range(0, len(ListaTotal)):
        if ListaTotal[i][0] == v:
            return i
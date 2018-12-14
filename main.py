import utilitarios as ut

arquivo=input("Qual o nome do arquivo ?")
Grafo, classificacao = ut.OpenFile(
    arquivo)  # pego o arquivo txt e passo para a variavel grafo e a classificacao do grafo para variavel classificacao

string = Grafo.split()
string2 = Grafo.split("\n")

ListVertices = ut.vertices(string, classificacao)
ListaTotal = []

for i in ListVertices:
    ListaTotal.append([i])
ListaTotal = sorted(ListaTotal)
# a logica aqui para fazer a lista de adjacentes é ter uma lista em outra lista do tipo [[],[],[]]  tal que cada elemento
# da lista total será composta de uma lista em que sua primeira posição possui o nome do Vertice e nas posições posteriores
# possuem os vertices adjacentes a ele // EXEMPLO : [[v1,object1,object2],[v2,object2]] os objetos possuem o nome do vertice
# adjacente e o valor da sua aresta.
ListaTotal = ut.FazerListaTotal(ListaTotal, string2, classificacao)
print("\n----LISTA DE ADJACENCIAS----")
for i in ListaTotal:
    print("Vertice [{}]".format(i[0]))
    for j in range(1, len(i)):
        print("Adjacencias= Vertice:{} Aresta:{}".format(i[j].getVertice(), i[j].getAresta()))
flag=0
while (flag==0):
    menu=int(input("\nBusca Em Profundidade[1]\nDijkstra[2]\nSair[3]")) #escolhe qual algoritmo usar

    if menu==1:
        busca = (input("Qual o vertice voce quer começar a busca?"))
        niveis = ut.BuscaProfundidade(busca, ListaTotal, ListVertices)

        saida = open('arquivosaida.txt', 'w')
        for i in range(0, len(niveis)):
            for j in range(i + 1, len(niveis)):
                if niveis[i] == niveis[j]:
                    saida.write('{} {}/{}\n'.format(niveis[i], i, j))
        saida.close()
        print("\nArquivo com o Nível de cada vértice gerado.\n")

    if menu==2:
        vertice = input("Qual o vertice inicial?")
        vertice2=input("Qual o vertice final?")
        d = ut.Dijkstra(ListaTotal, vertice)
        for i in range(0,len(ListaTotal)):
            if ListaTotal[i][0]==vertice2:
                aux=i
        if d[aux]<float('inf'):
            print("\nA distancia de {} para {} : {} \n".format(vertice,vertice2,d[aux]))
        else:
            print("\nnão são conectados.\n")

    if menu==3:
        flag=1
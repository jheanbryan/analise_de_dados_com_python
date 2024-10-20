'''
Ordenar  com funçao pronta
lista = [2, 4, 45, 10, 1]

lista_ordenada1 = sorted(lista)
lista_ordenada2 = lista.sort()
print(lista_ordenada1)


Ordenar lista pequena
lista = [7, 4]
if lista[0] > lista[1]:
    aux = lista[1]
    lista[1] = lista[0]
    lista[0] = aux

print(lista)


Selection sort
Iteração 1: percorre toda a lista, procurando o menor valor para ocupar a posição 0.
Iteração 2: a partir da posição 1, percorre toda a lista, procurando o menor valor para ocupar a posição 1.
Iteração 3: a partir da posição 2, percorre toda a lista, procurando o menor valor para ocupar a posição 2.
Esse processo é repetido N-1 vezes, sendo N o tamanho da lista.

def executar_selection_sort(lista):
    n = len(lista)
    
    for i in range(0, n):
        index_menor = i

        for j in range(i+1, n):
            if lista[j] < lista[index_menor]:
                index_menor = j
        lista[i], lista[index_menor] = lista[index_menor], lista[i]
    return lista


lista = [10, 9, 5, 8, 11, -1, 3]

executar_selection_sort(lista)
print(lista)


Bubble Sort
Iteração 1: seleciona o valor na posição 0 e o compara com seu vizinho – se for menor, há troca; se não for, seleciona o próximo e compara, repentindo o processo.
Iteração 2: seleciona o valor na posição 0 e compara ele com seu vizinho, se for menor troca, senão seleciona o próximo e compara, repentindo o processo.
Iteração N - 1: seleciona o valor na posição 0 e o compara com seu vizinho – se for menor, há troca; se não for, seleciona o próximo e compara, repentindo o processo.
def executar_bubble_sort(lista):
  n = len(lista)

  for i in range(n-1):
    for j in range(n-1):
      if lista[j] > lista[j+1]:
        aux = lista[j]
        lista[j] = lista[j+1] 
        lista [j+1] = aux
  print(lista)
  

lista = [45, 12, 78, 4, 56, 23, 89, 3, 15, 67, 34, 82, 55, 29, 91, 10, 38, 74, 92, 21]
executar_bubble_sort(lista)


'''





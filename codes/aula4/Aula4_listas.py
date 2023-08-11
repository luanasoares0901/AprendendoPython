#Listas

carros = ["Fusca", "Chevete","Kombi","Pampa"]
print(carros)

print(carros[0]) #imprimir carros na primeira posição
print(type(carros)) #vai imprimir o tipo da variável carros

#inserir mais um carro na lista
carros.append("Opala")
print(carros)


#remover algum item
carros.remove("Kombi")
print(carros)

#adicionar em uma posição específica
carros.insert(1,"Belina Del Rey") #na posição 1
print(carros)

#saber o tamanho da lista
print(len(carros))

#editar um dos itens
carros[1]="Belina Del-Rey"
print(carros)